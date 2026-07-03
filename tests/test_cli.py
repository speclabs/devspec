from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

from devspec_installer import __version__
from devspec_installer.cli import (
    Payload,
    classify_ownership,
    create_sync_plan,
    diff_files,
    main,
    sha256_file,
    should_exclude_payload,
    version_status,
)


def test_profiles_resolve_core_and_all_payloads() -> None:
    payload = Payload()

    core_paths = {str(item.path) for item in payload.resolve_profile_files("core")}
    all_paths = {str(item.path) for item in payload.resolve_profile_files("all")}

    assert "devspec/adapters/command-registry.md" in core_paths
    assert "devspec/architecture/_template/architecture-diagram.svg" in core_paths
    assert "devspec/architecture/_template/process-flow-diagram.svg" in core_paths
    assert "devspec/architecture/_template/diagram.html" in core_paths
    assert "devspec/architecture/_template/diagram.svg" not in core_paths
    assert "devspec/architecture/images/README.md" in core_paths
    assert "devspec/architecture/html/README.md" in core_paths
    assert ".github/prompts/devspec.story.prompt.md" in core_paths
    assert ".github/agents/devspec.story.agent.md" in core_paths
    assert not any(path.startswith(".github/workflows/") for path in core_paths)
    assert not any(path.startswith(".github/workflows/") for path in all_paths)
    assert "AGENTS.md" in core_paths
    assert "README.md" not in core_paths
    assert "docs/how-to/README.md" not in core_paths
    assert "docs/how-to/README.md" not in all_paths
    assert ".claude/skills/devspec-story/SKILL.md" in all_paths
    assert ".gemini/commands/devspec/story.toml" in all_paths
    assert ".agents/skills/devspec-story.md" in all_paths


def test_payload_excludes_github_workflows_even_from_broad_patterns() -> None:
    payload = Payload()
    payload.profiles["broad-github"] = {
        "description": "Temporary broad GitHub pattern for regression coverage.",
        "includes": [".github/**"],
    }

    paths = {str(item.path) for item in payload.resolve_profile_files("broad-github")}

    assert ".github/prompts/devspec.story.prompt.md" in paths
    assert ".github/agents/devspec.story.agent.md" in paths
    assert not any(path.startswith(".github/workflows/") for path in paths)
    assert should_exclude_payload(PurePosixPath(".github/workflows/python-package-ci.yml"))


def test_ownership_classification_preserves_project_artifacts() -> None:
    assert classify_ownership(PurePosixPath("devspec/foundation/project-context.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/overview.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/images/dia-001-system-context.svg")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/html/dia-001-system-context.html")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/_template/architecture-diagram.svg")) == "framework-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/_template/process-flow-diagram.svg")) == "framework-owned"
    assert classify_ownership(PurePosixPath("devspec/constitution.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/work-items/123-example/story.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/work-items/_template/story.md")) == "framework-owned"
    assert classify_ownership(PurePosixPath(".github/prompts/devspec.story.prompt.md")) == "framework-owned"


def test_svg_diagram_templates_are_standalone_xml() -> None:
    templates = sorted(Path("devspec/architecture/_template").glob("*.svg"))
    assert templates

    for template in templates:
        text = template.read_text(encoding="utf-8")
        lowered = text.lower()
        root = ET.fromstring(text)

        assert root.tag.endswith("svg")
        assert root.attrib["viewBox"]
        assert root.attrib["role"] == "img"
        assert root.attrib["aria-labelledby"] == "title desc"
        assert "http://www.w3.org/2000/svg" in root.tag
        assert root.find("{http://www.w3.org/2000/svg}title") is not None
        assert root.find("{http://www.w3.org/2000/svg}desc") is not None
        assert text.isascii()
        for forbidden in ("<script", "<iframe", "<foreignobject", "<image", "@import", "href=\"http", "href='http"):
            assert forbidden not in lowered


def test_html_diagram_template_is_standalone_static_html() -> None:
    template = Path("devspec/architecture/_template/diagram.html")
    text = template.read_text(encoding="utf-8")
    lowered = text.lower()

    assert lowered.startswith("<!doctype html>")
    assert text.isascii()
    for forbidden in ("<script", "<iframe", "http://", "https://"):
        assert forbidden not in lowered


def test_process_flow_svg_template_has_clean_ascii_source() -> None:
    template = Path("devspec/architecture/_template/process-flow-diagram.svg")
    text = template.read_text(encoding="utf-8")

    assert text.isascii()
    for mojibake in ("\u00e2", "\u00c3", "\ufffd"):
        assert mojibake not in text
    for process_role in ("step-manual", "step-automated", "step-integration", "decision", "exception-node", "artifact"):
        assert process_role in text


def test_init_writes_manifest_and_doctor_passes(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    assert (target / "devspec/adapters/command-registry.md").exists()
    assert (target / ".github/prompts/devspec.story.prompt.md").exists()

    manifest_path = target / "devspec/.install-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["profile"] == "core"
    assert manifest["repo_state"] == "existing"
    assert any(entry["path"] == "AGENTS.md" for entry in manifest["files"])

    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0


def test_init_refuses_conflicting_file(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    prompt = target / ".github/prompts/devspec.story.prompt.md"
    prompt.parent.mkdir(parents=True)
    prompt.write_text("local change\n", encoding="utf-8")

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 1


def test_sync_dry_run_preserves_project_owned_files(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    project_file = target / "devspec/foundation/project-context.md"
    project_file.write_text("# Local Project Context\n", encoding="utf-8")

    assert main(["sync", "--target", str(target), "--profile", "core", "--dry-run"]) == 0
    assert project_file.read_text(encoding="utf-8") == "# Local Project Context\n"


def test_diff_detects_modified_framework_file(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "new"]) == 0
    prompt = target / ".github/prompts/devspec.story.prompt.md"
    prompt.write_text("local prompt change\n", encoding="utf-8")

    assert main(["diff", "--target", str(target), "--profile", "core"]) == 1


def test_version_status_classification() -> None:
    assert version_status(None).status == "not-installed"
    assert version_status({"devspec_version": __version__}).status == "same"
    assert version_status({"devspec_version": "0.0.1"}).status == "upgrade"
    assert version_status({"devspec_version": "999.0.0"}).status == "downgrade"
    assert version_status({"devspec_version": "not-a-version"}).status == "unknown"
    assert version_status({}).status == "unknown"


def test_diff_prints_version_summary(tmp_path: Path, capsys) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    capsys.readouterr()

    assert main(["diff", "--target", str(target), "--profile", "core"]) == 0
    output = capsys.readouterr().out
    assert f"Installed version: {__version__}" in output
    assert f"Package version: {__version__}" in output
    assert "Version status: up to date" in output


def test_diff_and_doctor_default_to_manifest_profile(tmp_path: Path, capsys) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    capsys.readouterr()

    assert main(["diff", "--target", str(target)]) == 0
    diff_output = capsys.readouterr().out
    assert "Profile mismatches" not in diff_output

    assert main(["doctor", "--target", str(target)]) == 0
    doctor_output = capsys.readouterr().out
    assert "devspec doctor passed for profile 'core'" in doctor_output


def test_sync_dry_run_prints_version_summary_without_mutating_manifest(tmp_path: Path, capsys) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    manifest_path = target / "devspec/.install-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["devspec_version"] = "0.0.1"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    before = manifest_path.read_text(encoding="utf-8")
    capsys.readouterr()

    assert main(["sync", "--target", str(target), "--profile", "core", "--dry-run"]) == 0
    output = capsys.readouterr().out
    assert "Installed version: 0.0.1" in output
    assert f"Package version: {__version__}" in output
    assert "Version status: upgrade available" in output
    assert manifest_path.read_text(encoding="utf-8") == before


def test_sync_updates_manifest_version_after_success(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    manifest_path = target / "devspec/.install-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["devspec_version"] = "0.0.1"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    assert main(["sync", "--target", str(target), "--profile", "core"]) == 0
    updated = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert updated["devspec_version"] == __version__


def test_doctor_warns_for_version_states(tmp_path: Path, capsys) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    manifest_path = target / "devspec/.install-manifest.json"
    capsys.readouterr()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["devspec_version"] = "0.0.1"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0
    assert "is older than package version" in capsys.readouterr().out

    manifest["devspec_version"] = "999.0.0"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0
    assert "is newer than package version" in capsys.readouterr().out

    manifest["devspec_version"] = "invalid"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0
    assert "manifest devspec_version is missing or invalid" in capsys.readouterr().out

    manifest.pop("devspec_version")
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0
    assert "manifest devspec_version is missing or invalid" in capsys.readouterr().out


def test_missing_manifest_version_warnings_do_not_fail_doctor(tmp_path: Path, capsys) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["doctor", "--target", str(target), "--profile", "core"]) == 0
    assert "install manifest is missing" in capsys.readouterr().out


def test_checksum_not_version_decides_stale_and_writable_files(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    payload = Payload()
    files = payload.resolve_profile_files("core")
    manifest_path = target / "devspec/.install-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    manifest["devspec_version"] = "0.0.1"
    report = diff_files(files, target, manifest, "core")
    assert report["stale"] == []
    assert report["modified"] == []

    target_prompt = target / ".github/prompts/devspec.story.prompt.md"
    target_prompt.write_text("old installed prompt\n", encoding="utf-8")
    old_hash = sha256_file(target_prompt)
    for entry in manifest["files"]:
        if entry["path"] == ".github/prompts/devspec.story.prompt.md":
            entry["sha256"] = old_hash
            break

    report = diff_files(files, target, manifest, "core")
    assert ".github/prompts/devspec.story.prompt.md" in report["stale"]
    plan = create_sync_plan(files, target, manifest, force=False)
    assert ".github/prompts/devspec.story.prompt.md" in {str(item.path) for item in plan.files}


def test_checksum_detects_modified_conflict_despite_version_mismatch(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()

    assert main(["init", "--target", str(target), "--profile", "core", "--repo-state", "existing"]) == 0
    payload = Payload()
    files = payload.resolve_profile_files("core")
    manifest_path = target / "devspec/.install-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["devspec_version"] = "0.0.1"

    target_prompt = target / ".github/prompts/devspec.story.prompt.md"
    target_prompt.write_text("local prompt edit\n", encoding="utf-8")

    report = diff_files(files, target, manifest, "core")
    assert ".github/prompts/devspec.story.prompt.md" in report["modified"]
    plan = create_sync_plan(files, target, manifest, force=False)
    assert ".github/prompts/devspec.story.prompt.md has local changes" in plan.conflicts
