from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib import resources
from pathlib import Path, PurePosixPath
from typing import Iterable

from . import __version__


MANIFEST_PATH = PurePosixPath("devspec/.install-manifest.json")
PROFILES_PATH = PurePosixPath("packaging/devspec-profiles.json")

FRAMEWORK_OWNED = "framework-owned"
PROJECT_OWNED = "project-owned"


@dataclass(frozen=True)
class PayloadFile:
    path: PurePosixPath
    source: Path
    ownership: str
    digest: str


@dataclass(frozen=True)
class CopyPlan:
    files: list[PayloadFile]
    conflicts: list[str]
    skipped: list[str]


@dataclass(frozen=True)
class VersionStatus:
    installed: str | None
    package: str
    status: str
    label: str


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        return args.func(args)
    except DevspecError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devspec",
        description="Install, diff, sync, and validate devspec framework files.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    version_parser = subparsers.add_parser("version", help="Print the devspec CLI version.")
    version_parser.set_defaults(func=cmd_version)

    init_parser = subparsers.add_parser("init", help="Install devspec files into a target repository.")
    add_target(init_parser)
    add_profile(init_parser)
    init_parser.add_argument("--repo-state", choices=["new", "existing"], required=True)
    init_parser.add_argument("--force", action="store_true", help="Overwrite conflicting framework files.")
    init_parser.set_defaults(func=cmd_init)

    diff_parser = subparsers.add_parser("diff", help="Compare target files with the packaged framework.")
    add_target(diff_parser)
    add_profile(diff_parser, required=False)
    diff_parser.set_defaults(func=cmd_diff)

    sync_parser = subparsers.add_parser("sync", help="Update installed framework-owned files.")
    add_target(sync_parser)
    add_profile(sync_parser)
    sync_parser.add_argument("--dry-run", action="store_true", help="Show planned changes without writing files.")
    sync_parser.add_argument("--force", action="store_true", help="Overwrite modified framework-owned files.")
    sync_parser.set_defaults(func=cmd_sync)

    doctor_parser = subparsers.add_parser("doctor", help="Validate a devspec installation.")
    add_target(doctor_parser)
    add_profile(doctor_parser, required=False)
    doctor_parser.set_defaults(func=cmd_doctor)

    return parser


def add_target(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--target", default=".", help="Target repository root. Defaults to current directory.")


def add_profile(parser: argparse.ArgumentParser, required: bool = True) -> None:
    parser.add_argument("--profile", default=None, required=required, help="Install profile.")


def cmd_version(_args: argparse.Namespace) -> int:
    print(__version__)
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    payload = Payload()
    target = resolve_target(args.target)
    files = payload.resolve_profile_files(args.profile)
    plan = create_copy_plan(files, target, force=args.force, mode="init")

    if plan.conflicts:
        print_report("Conflicts", plan.conflicts)
        print("No files were written. Re-run with --force only after reviewing the conflicts.")
        return 1

    written = write_files(plan.files, target, dry_run=False)
    manifest = build_manifest(args.profile, args.repo_state, plan.files)
    write_manifest(target, manifest)

    print(f"Installed devspec profile '{args.profile}' into {target}")
    print(f"Files written: {written}")
    if plan.skipped:
        print_report("Skipped unchanged files", plan.skipped)
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    payload = Payload()
    target = resolve_target(args.target)
    profile = args.profile or profile_from_manifest(target) or "all"
    files = payload.resolve_profile_files(profile)
    manifest = read_manifest(target)
    report = diff_files(files, target, manifest, profile)

    print_version_status(version_status(manifest))
    print_diff_report(report)
    return 1 if report["missing"] or report["modified"] or report["stale"] or report["profile"] else 0


def cmd_sync(args: argparse.Namespace) -> int:
    payload = Payload()
    target = resolve_target(args.target)
    manifest = read_manifest(target)
    files = payload.resolve_profile_files(args.profile)

    plan = create_sync_plan(files, target, manifest, force=args.force)
    if plan.conflicts:
        print_version_status(version_status(manifest))
        print_report("Conflicts", plan.conflicts)
        print("No files were written. Run with --dry-run first, then use --force only for reviewed framework-owned files.")
        return 1

    if args.dry_run:
        print_version_status(version_status(manifest))
        print(f"Dry run for devspec profile '{args.profile}' in {target}")
        print(f"Files that would be written: {len(plan.files)}")
    else:
        written = write_files(plan.files, target, dry_run=False)
        repo_state = manifest.get("repo_state", "existing") if manifest else "existing"
        write_manifest(target, build_manifest(args.profile, repo_state, files))
        print_version_status(version_status(manifest))
        print(f"Synchronized devspec profile '{args.profile}' in {target}")
        print(f"Files written: {written}")
    if plan.skipped:
        print_report("Skipped files", plan.skipped)
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    payload = Payload()
    target = resolve_target(args.target)
    profile = args.profile or profile_from_manifest(target) or "all"
    files = payload.resolve_profile_files(profile)
    installed_paths = {str(item.path) for item in files}

    errors: list[str] = []
    warnings: list[str] = []

    for item in files:
        if not item.source.exists():
            errors.append(f"profile '{profile}' references missing payload file: {item.path}")

    manifest = read_manifest(target)
    status = version_status(manifest)
    if manifest is None:
        warnings.append(f"install manifest is missing: {MANIFEST_PATH}")
    else:
        manifest_profile = manifest.get("profile")
        if manifest_profile and manifest_profile != profile:
            warnings.append(f"profile mismatch: manifest has '{manifest_profile}', doctor checked '{profile}'")
    if status.status == "unknown":
        warnings.append("manifest devspec_version is missing or invalid")
    elif status.status == "upgrade":
        warnings.append(f"installed devspec version '{status.installed}' is older than package version '{status.package}'")
    elif status.status == "downgrade":
        warnings.append(f"installed devspec version '{status.installed}' is newer than package version '{status.package}'")

    for item in files:
        if not (target / as_local_path(item.path)).exists():
            warnings.append(f"target is missing installed file: {item.path}")

    validate_command_registry(payload, installed_paths, errors)
    validate_adapter_wrappers(profile, payload, installed_paths, errors)

    if errors:
        print_report("Errors", errors)
    if warnings:
        print_report("Warnings", warnings)
    if not errors and not warnings:
        print(f"devspec doctor passed for profile '{profile}' in {target}")
    return 1 if errors else 0


class DevspecError(RuntimeError):
    pass


class Payload:
    def __init__(self) -> None:
        self.root = find_source_root() or materialized_resource_root()
        self.profiles = self._load_profiles()

    def _load_profiles(self) -> dict:
        path = self.root / as_local_path(PROFILES_PATH)
        if not path.exists():
            raise DevspecError(f"profile manifest not found in payload: {PROFILES_PATH}")
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        profiles = data.get("profiles")
        if not isinstance(profiles, dict):
            raise DevspecError("profile manifest must contain a 'profiles' object")
        return profiles

    def resolve_profile_files(self, profile: str) -> list[PayloadFile]:
        if profile not in self.profiles:
            available = ", ".join(sorted(self.profiles))
            raise DevspecError(f"unknown profile '{profile}'. Available profiles: {available}")

        patterns = self._resolve_patterns(profile, seen=set())
        paths: dict[PurePosixPath, PayloadFile] = {}
        for pattern in patterns:
            for path in iter_pattern_matches(self.root, pattern):
                rel = to_posix(path.relative_to(self.root))
                if should_exclude_payload(rel):
                    continue
                paths[rel] = PayloadFile(
                    path=rel,
                    source=path,
                    ownership=classify_ownership(rel),
                    digest=sha256_file(path),
                )
        return [paths[key] for key in sorted(paths)]

    def _resolve_patterns(self, profile: str, seen: set[str]) -> list[str]:
        if profile in seen:
            raise DevspecError(f"cyclic profile inheritance at '{profile}'")
        branch = {*seen, profile}
        data = self.profiles[profile]
        patterns: list[str] = []
        for parent in data.get("extends", []):
            patterns.extend(self._resolve_patterns(parent, branch))
        patterns.extend(data.get("includes", []))
        return patterns


def find_source_root() -> Path | None:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "devspec/adapters/command-registry.md").exists() and (parent / "packaging/devspec-profiles.json").exists():
            return parent
    return None


def materialized_resource_root() -> Path:
    resource = resources.files("devspec_installer").joinpath("payload")
    if not resource.is_dir():
        raise DevspecError("packaged payload is missing")
    return Path(str(resource))


def iter_pattern_matches(root: Path, pattern: str) -> Iterable[Path]:
    normalized = pattern.replace("\\", "/")
    if normalized.endswith("/**"):
        base = root / as_local_path(PurePosixPath(normalized[:-3]))
        if base.exists():
            yield from (path for path in base.rglob("*") if path.is_file())
        return

    candidate = root / as_local_path(PurePosixPath(normalized))
    if candidate.is_file():
        yield candidate
        return
    if candidate.is_dir():
        yield from (path for path in candidate.rglob("*") if path.is_file())
        return

    for path in root.rglob("*"):
        if path.is_file() and fnmatch.fnmatch(str(to_posix(path.relative_to(root))), normalized):
            yield path


def should_exclude_payload(path: PurePosixPath) -> bool:
    parts = path.parts
    if any(part in {".git", ".vs", "__pycache__", ".pytest_cache", ".ruff_cache", "dist", "build"} for part in parts):
        return True
    if path.name.endswith((".pyc", ".pyo")):
        return True
    if path == MANIFEST_PATH:
        return True
    return False


def classify_ownership(path: PurePosixPath) -> str:
    parts = path.parts
    if path in {PurePosixPath("devspec/constitution.md"), PurePosixPath("devspec/glossary.md")}:
        return PROJECT_OWNED
    if len(parts) == 3 and parts[0] == "devspec" and parts[1] == "foundation" and path.suffix == ".md":
        return PROJECT_OWNED
    if len(parts) == 3 and parts[0] == "devspec" and parts[1] == "architecture" and path.suffix == ".md":
        return PROJECT_OWNED
    if len(parts) >= 4 and parts[:3] == ("devspec", "architecture", "diagrams") and path.suffix == ".md":
        return PROJECT_OWNED
    if len(parts) >= 4 and parts[:3] == ("devspec", "architecture", "images") and path.suffix == ".svg":
        return PROJECT_OWNED
    if len(parts) >= 3 and parts[:2] == ("devspec", "work-items") and parts[2] != "_template":
        return PROJECT_OWNED
    return FRAMEWORK_OWNED


def create_copy_plan(files: list[PayloadFile], target: Path, force: bool, mode: str) -> CopyPlan:
    conflicts: list[str] = []
    skipped: list[str] = []
    writable: list[PayloadFile] = []
    for item in files:
        destination = target / as_local_path(item.path)
        if not destination.exists():
            writable.append(item)
            continue
        destination_hash = sha256_file(destination)
        if destination_hash == item.digest:
            skipped.append(str(item.path))
            continue
        if item.ownership == PROJECT_OWNED and mode == "sync":
            skipped.append(f"{item.path} (project-owned)")
            continue
        if force and item.ownership == FRAMEWORK_OWNED:
            writable.append(item)
            continue
        conflicts.append(f"{item.path} already exists and differs")
    return CopyPlan(files=writable, conflicts=conflicts, skipped=skipped)


def create_sync_plan(files: list[PayloadFile], target: Path, manifest: dict | None, force: bool) -> CopyPlan:
    conflicts: list[str] = []
    skipped: list[str] = []
    writable: list[PayloadFile] = []
    manifest_files = {entry["path"]: entry for entry in (manifest or {}).get("files", []) if isinstance(entry, dict) and "path" in entry}

    for item in files:
        destination = target / as_local_path(item.path)
        if item.ownership == PROJECT_OWNED and destination.exists():
            skipped.append(f"{item.path} (project-owned)")
            continue
        if not destination.exists():
            writable.append(item)
            continue
        destination_hash = sha256_file(destination)
        if destination_hash == item.digest:
            skipped.append(str(item.path))
            continue
        previous = manifest_files.get(str(item.path), {}).get("sha256")
        if previous and destination_hash == previous:
            writable.append(item)
            continue
        if force and item.ownership == FRAMEWORK_OWNED:
            writable.append(item)
            continue
        conflicts.append(f"{item.path} has local changes")
    return CopyPlan(files=writable, conflicts=conflicts, skipped=skipped)


def write_files(files: list[PayloadFile], target: Path, dry_run: bool) -> int:
    count = 0
    for item in files:
        destination = target / as_local_path(item.path)
        if dry_run:
            count += 1
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(item.source, destination)
        count += 1
    return count


def build_manifest(profile: str, repo_state: str, files: list[PayloadFile]) -> dict:
    return {
        "schema_version": 1,
        "devspec_version": __version__,
        "profile": profile,
        "repo_state": repo_state,
        "installed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "files": [
            {
                "path": str(item.path),
                "sha256": item.digest,
                "ownership": item.ownership,
            }
            for item in sorted(files, key=lambda value: value.path)
        ],
    }


def write_manifest(target: Path, manifest: dict) -> None:
    path = target / as_local_path(MANIFEST_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_manifest(target: Path) -> dict | None:
    path = target / as_local_path(MANIFEST_PATH)
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def profile_from_manifest(target: Path) -> str | None:
    manifest = read_manifest(target)
    if not manifest:
        return None
    profile = manifest.get("profile")
    return profile if isinstance(profile, str) else None


def version_status(manifest: dict | None) -> VersionStatus:
    if manifest is None:
        return VersionStatus(installed=None, package=__version__, status="not-installed", label="not installed")

    installed = manifest.get("devspec_version")
    if not isinstance(installed, str):
        return VersionStatus(installed=None, package=__version__, status="unknown", label="unknown")

    installed_version = parse_semver(installed)
    package_version = parse_semver(__version__)
    if installed_version is None or package_version is None:
        return VersionStatus(installed=installed, package=__version__, status="unknown", label="unknown")
    if installed_version == package_version:
        return VersionStatus(installed=installed, package=__version__, status="same", label="up to date")
    if installed_version < package_version:
        return VersionStatus(installed=installed, package=__version__, status="upgrade", label="upgrade available")
    return VersionStatus(installed=installed, package=__version__, status="downgrade", label="newer than package")


def parse_semver(value: str) -> tuple[int, int, int] | None:
    parts = value.split(".")
    if len(parts) != 3:
        return None
    try:
        parsed = tuple(int(part) for part in parts)
    except ValueError:
        return None
    return parsed if all(part >= 0 for part in parsed) else None


def diff_files(files: list[PayloadFile], target: Path, manifest: dict | None, profile: str) -> dict[str, list[str]]:
    report = {"missing": [], "modified": [], "stale": [], "protected": [], "profile": []}
    manifest_files = {entry["path"]: entry for entry in (manifest or {}).get("files", []) if isinstance(entry, dict) and "path" in entry}

    if manifest and manifest.get("profile") != profile:
        report["profile"].append(f"manifest profile is '{manifest.get('profile')}', requested profile is '{profile}'")

    for item in files:
        destination = target / as_local_path(item.path)
        if item.ownership == PROJECT_OWNED:
            report["protected"].append(str(item.path))
        if not destination.exists():
            report["missing"].append(str(item.path))
            continue
        destination_hash = sha256_file(destination)
        if destination_hash == item.digest:
            continue
        previous = manifest_files.get(str(item.path), {}).get("sha256")
        if previous and destination_hash == previous:
            report["stale"].append(str(item.path))
        else:
            report["modified"].append(str(item.path))
    return report


def validate_command_registry(payload: Payload, installed_paths: set[str], errors: list[str]) -> None:
    registry = payload.root / "devspec/adapters/command-registry.md"
    if not registry.exists():
        errors.append("missing command registry in payload")
        return
    for line in registry.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `/devspec."):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        if len(columns) < 5:
            continue
        prompt = strip_markdown_code(columns[3])
        agent = strip_markdown_code(columns[4])
        for required in (prompt, agent):
            if required and required not in installed_paths:
                errors.append(f"registry references missing profile file: {required}")


def validate_adapter_wrappers(profile: str, payload: Payload, installed_paths: set[str], errors: list[str]) -> None:
    commands = command_names(payload)
    profiles_to_check = expanded_profile_names(payload, profile)

    if "claude" in profiles_to_check:
        for command in commands:
            name = command.removeprefix("/").replace(".", "-")
            required = f".claude/skills/{name}/SKILL.md"
            if required not in installed_paths:
                errors.append(f"Claude profile missing wrapper: {required}")
    if "gemini" in profiles_to_check:
        for command in commands:
            suffix = command.removeprefix("/devspec.")
            required = f".gemini/commands/devspec/{suffix}.toml"
            if required not in installed_paths:
                errors.append(f"Gemini profile missing wrapper: {required}")
    if "antigravity" in profiles_to_check:
        for command in commands:
            name = command.removeprefix("/").replace(".", "-")
            required = f".agents/skills/{name}.md"
            if required not in installed_paths:
                errors.append(f"Antigravity profile missing wrapper: {required}")
    if "cursor" in profiles_to_check and ".cursor/rules/devspec-workflow.mdc" not in installed_paths:
        errors.append("Cursor profile missing .cursor/rules/devspec-workflow.mdc")
    if "codex" in profiles_to_check and "AGENTS.md" not in installed_paths:
        errors.append("Codex profile missing AGENTS.md")


def command_names(payload: Payload) -> list[str]:
    registry = payload.root / "devspec/adapters/command-registry.md"
    names: list[str] = []
    for line in registry.read_text(encoding="utf-8").splitlines():
        if line.startswith("| `/devspec."):
            columns = [column.strip() for column in line.strip("|").split("|")]
            names.append(strip_markdown_code(columns[0]))
    return names


def expanded_profile_names(payload: Payload, profile: str) -> set[str]:
    names: set[str] = set()

    def visit(name: str) -> None:
        if name in names:
            return
        names.add(name)
        for parent in payload.profiles[name].get("extends", []):
            visit(parent)

    visit(profile)
    return names


def strip_markdown_code(value: str) -> str:
    return value.strip().strip("`")


def print_version_status(status: VersionStatus) -> None:
    if status.status == "not-installed":
        installed = "not installed"
    else:
        installed = status.installed or "unknown"
    print(f"Installed version: {installed}")
    print(f"Package version: {status.package}")
    print(f"Version status: {status.label}")


def print_diff_report(report: dict[str, list[str]]) -> None:
    empty = True
    for title, values in (
        ("Profile mismatches", report["profile"]),
        ("Missing files", report["missing"]),
        ("Modified files", report["modified"]),
        ("Stale files", report["stale"]),
        ("Protected project-owned files", report["protected"]),
    ):
        if values:
            empty = False
            print_report(title, values)
    if empty:
        print("No devspec differences found.")


def print_report(title: str, values: list[str]) -> None:
    print(f"{title}:")
    for value in values:
        print(f"  - {value}")


def resolve_target(value: str) -> Path:
    return Path(value).expanduser().resolve()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def to_posix(path: Path) -> PurePosixPath:
    return PurePosixPath(path.as_posix())


def as_local_path(path: PurePosixPath) -> Path:
    return Path(*path.parts)
