from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

from devspec_installer.cli import Payload, classify_ownership, main


def test_profiles_resolve_core_and_all_payloads() -> None:
    payload = Payload()

    core_paths = {str(item.path) for item in payload.resolve_profile_files("core")}
    all_paths = {str(item.path) for item in payload.resolve_profile_files("all")}

    assert "devspec/adapters/command-registry.md" in core_paths
    assert ".github/prompts/devspec.story.prompt.md" in core_paths
    assert ".github/agents/devspec.story.agent.md" in core_paths
    assert "AGENTS.md" in core_paths
    assert "README.md" not in core_paths
    assert "docs/how-to/README.md" not in core_paths
    assert "docs/how-to/README.md" not in all_paths
    assert ".claude/skills/devspec-story/SKILL.md" in all_paths
    assert ".gemini/commands/devspec/story.toml" in all_paths
    assert ".agents/skills/devspec-story.md" in all_paths


def test_ownership_classification_preserves_project_artifacts() -> None:
    assert classify_ownership(PurePosixPath("devspec/foundation/project-context.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/architecture/overview.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/constitution.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/work-items/123-example/story.md")) == "project-owned"
    assert classify_ownership(PurePosixPath("devspec/work-items/_template/story.md")) == "framework-owned"
    assert classify_ownership(PurePosixPath(".github/prompts/devspec.story.prompt.md")) == "framework-owned"


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
