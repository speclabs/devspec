"""Render, synchronize, and validate the compact framework tree."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

from . import __version__
from .definitions import COMMANDS, PROTOCOLS, canonical_root, install_files, lifecycle_commands, workflow_block

PROFILES = ("all", "copilot", "codex", "claude", "cursor", "gemini", "antigravity")
ADAPTERS = PROFILES[1:]
MANIFEST_PATH = Path("devspec/.install-manifest.json")
FRAMEWORK_OWNED = "framework-owned"
PROJECT_OWNED = "project-owned"


@dataclass(frozen=True)
class ManagedFile:
    path: Path
    content: str
    ownership: str

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.content.encode("utf-8")).hexdigest()



def write_file(path: Path, content: str, *, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") != content and not force:
        raise ValueError(f"Refusing to overwrite changed managed file: {path}")
    path.write_text(content, encoding="utf-8", newline="\n")


def wrapper_text(adapter: str, command) -> tuple[str, str]:
    contract = f"devspec/contracts/devspec.{command.name}.md"
    if adapter == "copilot":
        prompt = f"# devspec.{command.name}\n\nExecute `{contract}`. Use only its listed protocols.\n"
        agent = f"---\nname: devspec.{command.name}\ndescription: {command.purpose}\nuser-invocable: true\n---\nExecute `{contract}`.\n"
        return f".github/prompts/devspec.{command.name}.prompt.md", prompt + "\n---AGENT---\n" + agent
    if adapter == "claude":
        return f".claude/skills/devspec-{command.name}/SKILL.md", f"---\nname: devspec-{command.name}\ndescription: {command.purpose}\n---\nRead and execute `{contract}`.\n"
    if adapter == "gemini":
        return f".gemini/commands/devspec/{command.name}.toml", f"description = \"{command.purpose}\"\nprompt = \"Read and execute {contract}\"\n"
    if adapter == "antigravity":
        return f".agents/skills/devspec-{command.name}.md", f"---\nname: devspec-{command.name}\ndescription: {command.purpose}\n---\nRead and execute `{contract}`.\n"
    raise ValueError(adapter)


# Re-exported so existing callers keep importing it from here.
xml_block = workflow_block


def expected_paths(profile: str) -> list[Path]:
    # Validation consumes the installer payload so adapter coverage cannot drift.
    return [item.path for item in managed_payload(profile, "existing")]


# meta.md values a command rename left in existing work items. sync rewrites them; doctor reports them.
RENAMED_META_VALUES = {
    "stage": {"grooming": "refinement"},
    "next": {"devspec.grooming": "devspec.refine"},
    "resume": {"devspec.grooming": "devspec.refine"},
}


def migrate_renamed_meta(root: Path, *, dry_run: bool = False) -> list[str]:
    changes: list[str] = []
    for meta in sorted((root / "devspec/work-items").glob("*/meta.md")):
        if meta.parent.name == "_template":
            continue
        lines = meta.read_text(encoding="utf-8").splitlines(keepends=True)
        updated = []
        for line in lines:
            key, _, value = line.partition(":")
            new = RENAMED_META_VALUES.get(key.strip(), {}).get(value.strip())
            if new:
                changes.append(f"{meta.relative_to(root).as_posix()}: {key.strip()}: {value.strip()} -> {new}")
                line = f"{key.strip()}: {new}" + ("\n" if line.endswith("\n") else "")
            updated.append(line)
        if not dry_run and updated != lines:
            meta.write_text("".join(updated), encoding="utf-8", newline="\n")
    return changes


def doctor(root: Path, profile: str) -> list[str]:
    try:
        expected = expected_paths(profile)
    except OSError as exc:
        return [f"cannot read the canonical framework: {exc}"]
    issues = [f"missing: {path}" for path in expected if not (root / path).is_file()]
    for forbidden in ("devspec/work-items/current.md", "devspec/current-work-item.json"):
        if (root / forbidden).exists():
            issues.append(f"tracked current-work-item artifact is not allowed: {forbidden}")
    issues.extend(f"renamed work-item value: {change}; run devspec sync" for change in migrate_renamed_meta(root, dry_run=True))
    valid_stages = {"foundation", "intake", "refinement", "finalization", "tasks", "implementation", "review", "complete", "triage", "validation", "routed", "caller", "origin"}
    valid_runs = {"active", "blocked", "complete"}
    valid_next = {f"devspec.{command.name}" for command in COMMANDS} | {"none", "return-to-caller", "resume-origin"}
    lifecycle_templates = {
        "devspec/work-items/_template/meta.md": ("scope_revision:", "finalized_revision:", "planned_revision:", "implemented_revision:", "reviewed_revision:"),
        "devspec/work-items/_template/story.md": ("Source Record", "Immutable provider ID", "MCP resolution method", "User confirmation", "Raised by", "Affected Areas"), "devspec/work-items/_template/tasks.md": ("Scope revision:", "Source justification", "Done condition"), "devspec/work-items/_template/implement.md": ("Scope revision:", "Changed-work baseline:"), "devspec/work-items/_template/review.md": ("Scope revision:", "Changed-work baseline:"), "devspec/work-items/_template/clarify.md": ("Origin command", "Resolution", "Resume command"),
    }
    current_context_commands = {"story", "refine", "finalize", "tasks", "implement", "review", "clarify", "changerequest"}
    protocol_text_requirements = {
        "run": {"preflight": ("Before every command", "single-repository or multi-repository scope", "current workspace as proposed", "repo-access protocol", "Do not inspect or change source")},
        "repo-access": {
            "collect": ("free-form text input", "Confirm the path before asking about access"),
            "question": ("After each path is confirmed", "Custom Answer"),
            "recommend": ("exactly one choice recommended", "least-privilege"),
        },
        "current-work-item": {
            "location": ("git rev-parse --git-path devspec/current-work-item.json", "Never create or commit"),
            "record": ("work-item ID", "current branch", "selection source", "timestamp", "never committed or pushed"),
            "selection": ("validated explicit ID", "exactly one non-terminal work item on the current branch"),
            "validation": ("branch changed", "stage and next action"),
            "continuation": ("saved meta.md next action", "devspec.clarify", "terminal item is not resumed"),
            "clear": ("accepted review",),
        },
    }
    for name in PROTOCOLS:
        path = root / f"devspec/protocols/{name}.xml"
        if path.is_file():
            try:
                protocol = ElementTree.fromstring(path.read_text(encoding="utf-8"))
            except (ElementTree.ParseError, OSError, UnicodeDecodeError) as exc:
                issues.append(f"invalid XML: {path}: {exc}")
            else:
                required = {
                    "ask": ("when", "discovery", "sequence", "completion", "checkpoint", "interaction", "resolution"),
                    "run": ("preflight", "checkpoint", "context", "resume", "blocked", "closure"),
                    "work": ("scope", "evidence", "change", "artifacts"),
                    "repo-access": ("when", "collect", "question", "recommend", "record", "respect"),
                    "current-work-item": ("when", "location", "record", "selection", "validation", "recovery", "continuation", "update", "clear"),
                    "state": ("when", "run-states", "stages", "task-statuses", "evidence-labels", "resume"),
                }.get(name, ())
                present = {child.tag for child in protocol}
                missing = sorted(set(required) - present)
                if missing:
                    issues.append(f"missing protocol tags: {path}: {', '.join(missing)}")
                for tag, phrases in protocol_text_requirements.get(name, {}).items():
                    value = protocol.findtext(tag, default="")
                    for phrase in phrases:
                        if phrase not in value:
                            issues.append(f"missing protocol requirement: {path}: {tag}: {phrase}")
    for command in COMMANDS:
        path = root / f"devspec/contracts/devspec.{command.name}.md"
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
                workflow = ElementTree.fromstring(xml_block(text))
                if workflow.tag != "workflow" or workflow.attrib.get("command") != f"devspec.{command.name}":
                    issues.append(f"invalid contract identity: {path}")
                required = {"purpose", "protocols", "scope", "input", "rules", "entry", "outputs", "transitions", "closure"}
                present = {child.tag for child in workflow}
                missing = sorted(required - present)
                if missing:
                    issues.append(f"missing contract tags: {path}: {', '.join(missing)}")
                protocols = workflow.find("protocols")
                protocol_refs = {protocol.attrib.get("ref") for protocol in protocols} if protocols is not None else set()
                if command.name in current_context_commands and "current-work-item" not in protocol_refs:
                    issues.append(f"missing current-story protocol: {path}")
                if command.name != "story" and command.name in current_context_commands and "[work-item-id]" not in text:
                    issues.append(f"work-item ID is not optional: {path}")
            except (ValueError, ElementTree.ParseError, OSError, UnicodeDecodeError) as exc:
                issues.append(f"invalid contract XML: {path}: {exc}")
                continue
            outputs = workflow.find("outputs")
            if outputs is None or not list(outputs):
                issues.append(f"missing contract outputs: {path}")
            transitions = workflow.find("transitions")
            if transitions is None or not list(transitions):
                issues.append(f"missing contract transitions: {path}")
            else:
                for transition in transitions:
                    stage = transition.attrib.get("stage")
                    run = transition.attrib.get("run")
                    next_command = transition.attrib.get("next")
                    if not transition.attrib.get("outcome") or stage not in valid_stages or run not in valid_runs or next_command not in valid_next:
                        issues.append(f"invalid lifecycle transition: {path}")
                    if run == "blocked" and next_command != "devspec.clarify":
                        issues.append(f"blocked transition must clarify: {path}")
                    if next_command == "none" and run != "complete":
                        issues.append(f"terminal transition must be complete: {path}")
                    if run == "complete" and next_command != "none":
                        issues.append(f"complete transition must be terminal: {path}")
    registry = root / "devspec/command-registry.md"
    registry_text = registry.read_text(encoding="utf-8") if registry.is_file() else ""
    for command in COMMANDS:
        if f"devspec.{command.name}" not in registry_text:
            issues.append(f"missing registry command: devspec.{command.name}")
    for template, required_text in lifecycle_templates.items():
        text = (root / template).read_text(encoding="utf-8") if (root / template).is_file() else ""
        for expected in required_text:
            if expected not in text:
                issues.append(f"missing lifecycle template field: {template}: {expected}")
    adapters = ADAPTERS if profile == "all" else (profile,)
    for adapter in adapters:
        if adapter == "codex":
            text = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").is_file() else ""
            for command in COMMANDS:
                if f"devspec.{command.name}" not in text:
                    issues.append(f"missing Codex command reference: devspec.{command.name}")
        elif adapter == "cursor":
            path = root / ".cursor/rules/devspec-workflow.mdc"
            text = path.read_text(encoding="utf-8") if path.is_file() else ""
            for command in COMMANDS:
                if f"devspec.{command.name}" not in text:
                    issues.append(f"missing Cursor command reference: devspec.{command.name}")
        else:
            for command in COMMANDS:
                if adapter == "copilot":
                    paths = (root / f".github/prompts/devspec.{command.name}.prompt.md", root / f".github/agents/devspec.{command.name}.agent.md")
                elif adapter == "claude":
                    paths = (root / f".claude/skills/devspec-{command.name}/SKILL.md",)
                elif adapter == "gemini":
                    paths = (root / f".gemini/commands/devspec/{command.name}.toml",)
                else:
                    paths = (root / f".agents/skills/devspec-{command.name}.md",)
                expected = f"devspec/contracts/devspec.{command.name}.md"
                for path in paths:
                    if path.is_file():
                        text = path.read_text(encoding="utf-8")
                        if expected not in text:
                            issues.append(f"wrapper does not reference contract: {path}")
                        if "<workflow" in text:
                            issues.append(f"wrapper duplicates workflow logic: {path}")
    return issues


# Upgrade lifecycle. These definitions intentionally follow the compact installer
# above so existing callers retain their public import locations.
def _sha256(path: Path) -> str:
    # Hash normalized text so a CRLF checkout does not read as local drift.
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def _recorded_digests(path: Path) -> set[str]:
    # Releases before 0.3.0 recorded raw-byte digests, so an untouched file in a CRLF checkout
    # matches its manifest entry only byte for byte.
    return {_sha256(path), hashlib.sha256(path.read_bytes()).hexdigest()}


def _state_from_target(root: Path) -> str:
    state_file = root / "devspec/foundation/repository-state.md"
    if state_file.is_file():
        text = state_file.read_text(encoding="utf-8")
        if "State: new" in text:
            return "new"
    return "existing"


# Live project state seeded once from a template, then never overwritten by sync.
SEEDED_FROM_TEMPLATE = (
    (Path("devspec/architecture/overview.md"), "architecture/_template/overview.md"),
    (Path("devspec/architecture/artifact-queue.md"), "architecture/_template/artifact-queue.md"),
)


def _ownership(relative: Path) -> str:
    if relative == Path("constitution.md"):
        return PROJECT_OWNED
    if relative == Path("foundation/repository-state.md"):
        return PROJECT_OWNED
    return FRAMEWORK_OWNED


def managed_payload(profile: str, repo_state: str) -> tuple[ManagedFile, ...]:
    source_root = canonical_root()
    files: list[ManagedFile] = []
    for source in install_files():
        relative = source.relative_to(source_root)
        files.append(ManagedFile(Path("devspec") / relative, source.read_text(encoding="utf-8"), _ownership(relative)))
    route = "devspec.extract" if repo_state == "existing" else "devspec.projectcontext"
    files.append(ManagedFile(Path("devspec/foundation/repository-state.md"), f"# Repository State\n\n- State: {repo_state}\n- Start with: `{route}`\n", PROJECT_OWNED))
    # Seed the live architecture records from their templates. Installing the canonical copies
    # would hand every target repository this project's own diagram rows.
    for target, template in SEEDED_FROM_TEMPLATE:
        files.append(ManagedFile(target, (source_root / template).read_text(encoding="utf-8"), PROJECT_OWNED))
    adapters = ADAPTERS if profile == "all" else (profile,)
    for adapter in adapters:
        if adapter == "codex":
            command_lines = "\n".join(f"- `devspec.{c.name}`: read `devspec/contracts/devspec.{c.name}.md`." for c in lifecycle_commands())
            files.append(ManagedFile(Path("AGENTS.md"), "# devspec\n\nUse Git-tracked `devspec/` artifacts as canonical state. For a clear work-item continuation, resolve the per-worktree current context and run only its saved next action; ask before switching among multiple stories.\n\n" + command_lines + "\n", FRAMEWORK_OWNED))
        elif adapter == "cursor":
            commands = ", ".join(f"`devspec.{c.name}`" for c in lifecycle_commands())
            files.append(ManagedFile(Path(".cursor/rules/devspec-workflow.mdc"), f"---\ndescription: devspec workflow\nalwaysApply: false\n---\nFor {commands}, read the matching `devspec/contracts/` file and listed protocols. For a clear continuation, resolve per-worktree current context and run only the saved next action; ask before switching stories.\n", FRAMEWORK_OWNED))
        elif adapter == "copilot":
            for command in COMMANDS:
                prompt_path, combined = wrapper_text(adapter, command)
                prompt, agent = combined.split("\n---AGENT---\n", 1)
                files.extend((ManagedFile(Path(prompt_path), prompt, FRAMEWORK_OWNED), ManagedFile(Path(f".github/agents/devspec.{command.name}.agent.md"), agent, FRAMEWORK_OWNED)))
        else:
            for command in COMMANDS:
                wrapper_path, content = wrapper_text(adapter, command)
                files.append(ManagedFile(Path(wrapper_path), content, FRAMEWORK_OWNED))
    return tuple(sorted(files, key=lambda item: item.path.as_posix()))


def read_install_manifest(root: Path) -> dict | None:
    path = root / MANIFEST_PATH
    if not path.is_file():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def manifest_profile(root: Path) -> str | None:
    profile = (read_install_manifest(root) or {}).get("profile")
    return profile if profile in PROFILES else None


def _manifest_entries(manifest: dict | None, key: str = "files") -> dict[str, dict]:
    entries = (manifest or {}).get(key, [])
    return {entry["path"]: entry for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)}


def _write_manifest(root: Path, profile: str, repo_state: str, files: tuple[ManagedFile, ...], previous: dict | None = None) -> None:
    current = {item.path.as_posix() for item in files}
    retired = _manifest_entries(previous, "retained_obsolete")
    for path, entry in _manifest_entries(previous).items():
        if path not in current:
            retired[path] = entry
    # Only framework files retire. A project-owned record, such as a foundation artifact a 0.2.x
    # manifest tracked, is the team's own work and is never obsolete.
    retired = {path: entry for path, entry in retired.items() if path not in current and entry.get("ownership") != PROJECT_OWNED}
    data = {
        "schema_version": 1,
        "devspec_version": __version__,
        "profile": profile,
        "repo_state": repo_state,
        "installed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "files": [{"path": item.path.as_posix(), "sha256": item.digest, "ownership": item.ownership} for item in files],
        "retained_obsolete": [retired[key] for key in sorted(retired)],
    }
    manifest_path = root / MANIFEST_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _copy_plan(root: Path, files: tuple[ManagedFile, ...], previous: dict | None, *, mode: str, force: bool) -> tuple[list[ManagedFile], list[str], list[str]]:
    old = _manifest_entries(previous)
    writable: list[ManagedFile] = []
    conflicts: list[str] = []
    skipped: list[str] = []
    for item in files:
        target = root / item.path
        name = item.path.as_posix()
        if not target.exists():
            writable.append(item)
            continue
        digest = _sha256(target)
        if digest == item.digest:
            skipped.append(name)
            continue
        if item.ownership == PROJECT_OWNED:
            # A project-owned file that already exists is the developer's own work, and its
            # presence is expected when re-running init to add a profile. Never overwrite it,
            # and never fail on it: the only escape would be --force, which would destroy it.
            skipped.append(f"{name} (project-owned)")
            continue
        if mode == "sync" and old.get(name, {}).get("sha256") in _recorded_digests(target):
            writable.append(item)
        elif force:
            writable.append(item)
        else:
            conflicts.append(f"{name} has local changes" if mode == "sync" else f"{name} already exists and differs")
    return writable, conflicts, skipped


def _apply_files(root: Path, files: list[ManagedFile]) -> int:
    for item in files:
        write_file(root / item.path, item.content, force=True)
    return len(files)


def install_framework(root: Path, profile: str, repo_state: str, *, force: bool = False) -> None:
    previous = read_install_manifest(root)
    files = managed_payload(profile, repo_state)
    writable, conflicts, _ = _copy_plan(root, files, previous, mode="init", force=force)
    if conflicts:
        raise ValueError("; ".join(conflicts))
    _apply_files(root, writable)
    _write_manifest(root, profile, repo_state, files, previous)


def diff_framework(root: Path, profile: str) -> dict[str, list[str]]:
    manifest = read_install_manifest(root)
    files = managed_payload(profile, _state_from_target(root))
    old = _manifest_entries(manifest)
    report = {"profile": [], "missing": [], "modified": [], "stale": [], "protected": [], "obsolete": []}
    if manifest and manifest.get("profile") != profile:
        report["profile"].append(f"manifest profile is '{manifest.get('profile')}', requested profile is '{profile}'")
    for item in files:
        target = root / item.path
        name = item.path.as_posix()
        if item.ownership == PROJECT_OWNED and target.exists():
            report["protected"].append(name)
            continue
        if not target.exists():
            report["missing"].append(name)
            continue
        digest = _sha256(target)
        if digest == item.digest:
            continue
        if old.get(name, {}).get("sha256") in _recorded_digests(target):
            report["stale"].append(name)
        else:
            report["modified"].append(name)
    current = {item.path.as_posix() for item in files}
    tracked = {**_manifest_entries(manifest, "retained_obsolete"), **old}
    for name in sorted(tracked):
        if name not in current and tracked[name].get("ownership") != PROJECT_OWNED and (root / Path(name)).exists():
            report["obsolete"].append(name)
    return report


def sync_framework(root: Path, profile: str, *, dry_run: bool = False, force: bool = False) -> tuple[list[str], list[str], list[str], list[str]]:
    previous = read_install_manifest(root)
    state = _state_from_target(root)
    files = managed_payload(profile, state)
    obsolete = diff_framework(root, profile)["obsolete"]
    writable, conflicts, skipped = _copy_plan(root, files, previous, mode="sync", force=force)
    if not conflicts and not dry_run:
        _apply_files(root, writable)
        _write_manifest(root, profile, state, files, previous)
    return [item.path.as_posix() for item in writable], conflicts, skipped, obsolete


def doctor_warnings(root: Path, profile: str) -> list[str]:
    manifest = read_install_manifest(root)
    if not manifest:
        return [f"install manifest is missing: {MANIFEST_PATH.as_posix()}"]
    warnings: list[str] = []
    if manifest.get("profile") != profile:
        warnings.append(f"profile mismatch: manifest has '{manifest.get('profile')}', doctor checked '{profile}'")
    if manifest.get("devspec_version") != __version__:
        warnings.append(f"installed devspec version '{manifest.get('devspec_version', 'unknown')}' differs from package version '{__version__}'")
    return warnings
