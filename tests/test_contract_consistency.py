"""Cross-check the contracts against every surface that restates them.

The other suites install into a temporary directory and validate that, so drift between
this repository's own checked-in wrappers and its contracts stayed invisible. These tests
validate the repository itself.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from devspec.definitions import COMMANDS, LIFECYCLE_ORDER, PROTOCOLS, lifecycle_commands  # noqa: E402
from devspec.framework import FRAMEWORK_OWNED, doctor, managed_payload  # noqa: E402

CONTRACTS = REPO / "devspec/contracts"
# Live project state and this project's own work products are deliberately not installed.
UNINSTALLED = ("foundation/repository-state.md", "architecture/overview.md", "architecture/artifact-queue.md")
# The stages lifecycle.md tables. A transition into one of these moves a work item; caller,
# origin, foundation, triage and routed do not.
WORK_ITEM_STAGES = {"intake", "refinement", "finalization", "tasks", "implementation", "review", "complete"}


def contract_text(name: str) -> str:
    return (CONTRACTS / f"devspec.{name}.md").read_text(encoding="utf-8")


def workflow(name: str) -> ElementTree.Element:
    text = contract_text(name)
    return ElementTree.fromstring(text[text.index("<workflow"):text.index("</workflow>") + len("</workflow>")])


def table_rows(text: str, header_starts: str) -> list[list[str]]:
    rows = []
    seen_header = False
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            seen_header = False
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0].startswith(header_starts):
            seen_header = True
            continue
        if seen_header and not set("".join(cells)) <= set("-: "):
            rows.append(cells)
    return rows


class RepositoryIsCurrentTests(unittest.TestCase):
    def test_checked_in_wrappers_match_the_contracts(self) -> None:
        drift, checked = [], 0
        for item in managed_payload("all", "existing"):
            if item.ownership != FRAMEWORK_OWNED:
                continue
            target = REPO / item.path
            if not target.is_file():
                drift.append(f"{item.path.as_posix()} (missing)")
            elif target.read_text(encoding="utf-8") != item.content:
                drift.append(item.path.as_posix())
            else:
                checked += 1
        self.assertEqual([], drift, "run the installer to regenerate these from devspec/contracts")
        self.assertGreater(checked, len(COMMANDS), "expected at least one wrapper per command")

    def test_doctor_passes_against_this_repository(self) -> None:
        self.assertEqual([], doctor(REPO, "all"))

    def test_install_manifest_covers_every_canonical_file(self) -> None:
        from devspec.definitions import canonical_root, install_files

        root = canonical_root()
        installed = {p.relative_to(root).as_posix() for p in install_files()}
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(root).as_posix()
            if relative in UNINSTALLED or relative.startswith("quickfixes/QF-") or relative.startswith("work-items/") and "_template" not in relative:
                continue
            self.assertIn(relative, installed, f"{relative} is not covered by install-manifest.txt")


class ContractSchemaTests(unittest.TestCase):
    def test_every_command_has_a_lifecycle_position(self) -> None:
        self.assertEqual(sorted(LIFECYCLE_ORDER), sorted(c.name for c in COMMANDS))

    def test_heading_summary_matches_purpose(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                body = contract_text(command.name)
                summary = body[body.index("\n\n") + 2:body.index("\n\nInvocation:")].strip()
                self.assertEqual(command.purpose, summary)

    def test_derivable_elements_are_not_restated(self) -> None:
        # A workflow-level <artifact> restated <outputs>, <handoff> restated <transitions>, and
        # <actions> restated <rules>. The <artifact> child inside <outputs> is unaffected.
        for command in COMMANDS:
            with self.subTest(command.name):
                present = {child.tag for child in workflow(command.name)}
                self.assertEqual(set(), present & {"artifact", "handoff", "actions"})

    def test_every_contract_scopes_itself(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                scope = workflow(command.name).findtext("scope", default="").strip()
                self.assertTrue(scope, "contract must state when to use it and what to use instead")

    def test_protocol_refs_resolve(self) -> None:
        for command in COMMANDS:
            refs = list(workflow(command.name).find("protocols"))
            self.assertTrue(refs, f"{command.name} loads no protocol")
            for ref in refs:
                with self.subTest(command=command.name, ref=ref.attrib.get("ref")):
                    self.assertIn(ref.attrib.get("ref"), PROTOCOLS)

    def test_every_protocol_is_loaded_by_a_contract(self) -> None:
        used = {ref.attrib.get("ref") for c in COMMANDS for ref in workflow(c.name).find("protocols")}
        self.assertEqual(set(PROTOCOLS), used, "an unreferenced protocol never reaches the agent")

    def test_shared_vocabulary_reaches_every_command(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                refs = {ref.attrib.get("ref") for ref in workflow(command.name).find("protocols")}
                self.assertIn("state", refs)
                self.assertIn("run", refs)


class RouteGraphTests(unittest.TestCase):
    def transitions(self, name: str) -> list[dict]:
        return [t.attrib for t in workflow(name).find("transitions")]

    def test_blocked_and_terminal_transitions_agree_with_lifecycle(self) -> None:
        for command in COMMANDS:
            for attrib in self.transitions(command.name):
                with self.subTest(command=command.name, outcome=attrib.get("outcome")):
                    if attrib["run"] == "blocked":
                        self.assertEqual("devspec.clarify", attrib["next"])
                    if attrib["run"] == "complete":
                        self.assertEqual("none", attrib["next"])
                    if attrib["next"] == "none":
                        self.assertEqual("complete", attrib["run"])

    def test_finalize_returns_open_requirement_gaps_to_refine(self) -> None:
        # finalize once routed open gaps "through devspec.clarify to refinement", a route clarify
        # cannot take: it only resumes the command that recorded the blocker.
        returns = [t for t in self.transitions("finalize") if t["next"] == "devspec.refine"]
        self.assertEqual([("refinement", "active")], [(t["stage"], t["run"]) for t in returns])
        for command in COMMANDS:
            with self.subTest(command.name):
                self.assertNotIn("through devspec.clarify to", contract_text(command.name))

    def test_intake_and_change_requests_reach_finalize_only_through_refine(self) -> None:
        # Neither story nor changerequest reads the code, so neither may judge a story ready to finalize.
        for name in ("story", "changerequest"):
            with self.subTest(name):
                active = {t["next"] for t in self.transitions(name) if t["run"] == "active"}
                self.assertEqual({"devspec.refine"}, active)
        # An unclassified request is not yet part of the work item, so it must not move the item's stage.
        self.assertEqual({"active"}, {t["run"] for t in self.transitions("changerequest")})

    def test_finalize_asks_its_own_topics_and_hands_requirement_gaps_to_refine(self) -> None:
        # finalize owns security, compliance, and delivery questions, so it needs a full question
        # queue; requirement gaps it exposes go into story.md for refine, so it must write there.
        ask = next(p for p in workflow("finalize").find("protocols") if p.attrib["ref"] == "ask")
        self.assertNotIn("queue", ask.attrib)
        outputs = {a.attrib["path"] for a in workflow("finalize").find("outputs")}
        self.assertIn("devspec/work-items/<id>/story.md", outputs)

    def test_work_item_stages_match_the_lifecycle_table(self) -> None:
        text = (REPO / "devspec/lifecycle.md").read_text(encoding="utf-8")
        documented = {row[0].strip("`"): row[1] for row in table_rows(text, "Stage")}
        self.assertEqual(WORK_ITEM_STAGES, set(documented))
        for command in COMMANDS:
            for attrib in self.transitions(command.name):
                stage, nxt = attrib["stage"], attrib["next"]
                if stage in documented and nxt.startswith("devspec."):
                    with self.subTest(command=command.name, stage=stage):
                        self.assertIn(nxt, documented[stage], f"lifecycle.md does not allow {stage} -> {nxt}")

    def test_a_command_declares_the_records_it_writes(self) -> None:
        # ask.xml routes a blocker to a decision record; run.xml checkpoints the state record.
        for command in COMMANDS:
            outputs = [a.attrib["path"] for a in workflow(command.name).find("outputs")]
            stages = {t["stage"] for t in self.transitions(command.name)}
            runs = {t["run"] for t in self.transitions(command.name)}
            work_item = any(p.startswith("devspec/work-items/") for p in outputs)
            with self.subTest(command.name):
                if "blocked" in runs:
                    self.assertTrue(
                        any("decisions.md" in p for p in outputs) or any("QF-" in p for p in outputs),
                        f"{command.name} can block but declares no decision record",
                    )
                if work_item and stages & WORK_ITEM_STAGES:
                    self.assertTrue(
                        any(p.endswith("meta.md") for p in outputs),
                        f"{command.name} moves a work item but declares no meta.md",
                    )

    def test_a_contract_declares_every_artifact_its_rules_name(self) -> None:
        # devspec.finalize promoted decisions into two foundation artifacts it never declared.
        # Templates and protocols are read, never written, so they are not outputs.
        for command in COMMANDS:
            element = workflow(command.name)
            outputs = {a.attrib["path"] for a in element.find("outputs")}
            body = " ".join(
                ElementTree.tostring(element.find(tag), encoding="unicode")
                for tag in ("rules", "closure")
                if element.find(tag) is not None
            )
            named = set(re.findall(r"devspec/[A-Za-z0-9_./<>-]+\.(?:md|xml)", body))
            named = {p for p in named if "_template" not in p and "/protocols/" not in p}
            with self.subTest(command.name):
                self.assertEqual(set(), named - outputs, f"{command.name} writes an artifact it does not declare")

    def test_registry_restates_the_contracts_exactly(self) -> None:
        text = (REPO / "devspec/command-registry.md").read_text(encoding="utf-8")
        rows = table_rows(text, "Command")
        self.assertEqual([f"`devspec.{c.name}`" for c in lifecycle_commands()], [r[0] for r in rows])
        for command, row in zip(lifecycle_commands(), rows):
            with self.subTest(command.name):
                self.assertEqual(command.purpose, row[1])
                expected = []
                for attrib in self.transitions(command.name):
                    if attrib["next"] not in expected:
                        expected.append(attrib["next"])
                self.assertEqual(", ".join(f"`{v}`" for v in expected), row[2])


class DocumentationTests(unittest.TestCase):
    # A command a guide never names is a command a reader never finds.
    COVERING_DOCS = ("how-to.md", "command-examples.md", "quickstart.md", "workflows.md")

    def test_guides_do_not_contradict_the_refinement_route(self) -> None:
        # Guides kept offering a skip straight to finalize after the contracts made refinement the
        # only route out of intake.
        contract = contract_text("refine")
        self.assertIn("this is the only route out of intake", contract)
        pages = [REPO / "docs" / doc for doc in self.COVERING_DOCS]
        pages += [REPO / "README.md", REPO / "devspec/README.md", REPO / "docs/assets/delivery-routes.svg"]
        for page in pages:
            text = page.read_text(encoding="utf-8").lower()
            with self.subTest(page=page.name):
                for claim in ("refinement is optional", "refine when needed", "refine` when needed",
                              "refinement when needed", "optional refinement", "refinement, if needed",
                              "skip it only when", "skip it and run", "default step after intake"):
                    self.assertNotIn(claim, text, "refinement is the only route out of intake")

    def test_every_command_appears_in_the_command_guides(self) -> None:
        for doc in self.COVERING_DOCS:
            text = (REPO / "docs" / doc).read_text(encoding="utf-8")
            for command in COMMANDS:
                with self.subTest(doc=doc, command=command.name):
                    self.assertIn(f"devspec.{command.name}", text)


class ArtifactShapeTests(unittest.TestCase):
    def test_markdown_tables_are_well_formed(self) -> None:
        separator = re.compile(r"\|(\s*:?-+:?\s*\|)+$")
        broken, seen = [], 0
        roots = sorted((REPO / "devspec").rglob("*.md")) + sorted((REPO / "docs").rglob("*.md"))
        roots += [REPO / "README.md", REPO / "AGENTS.md"]
        for path in roots:
            lines = path.read_text(encoding="utf-8").split("\n")
            for index, line in enumerate(lines[:-1]):
                nxt = lines[index + 1].strip()
                if line.strip().startswith("|") and separator.fullmatch(nxt):
                    seen += 1
                    header = line.strip().strip("|").split("|")
                    if len(header) != len(nxt.strip("|").split("|")):
                        broken.append(f"{path.relative_to(REPO).as_posix()}:{index + 1}")
        self.assertEqual([], broken)
        self.assertGreater(seen, 30, "table scan found almost nothing; the walk is probably wrong")

    # Each entry is a field some contract or protocol names, and the template that must offer it.
    REQUIRED_FIELDS = {
        "devspec/foundation/_template/rules.md": ("Constitution principles",),
        "devspec/foundation/_template/tech-stack.md": ("Supported versions",),
        "devspec/foundation/_template/project-context.md": ("Evidence label",),
        "devspec/foundation/_template/codebase-structure.md": ("Integration points", "Validation location"),
        "devspec/architecture/_template/artifact-queue.md": ("Duplicate check",),
        "devspec/work-items/_template/story.md": ("Raised by", "Affected Areas"),
        "devspec/work-items/_template/finalize.md": ("CP-###", "Scope revision:"),
        "devspec/work-items/_template/tasks.md": ("Done condition", "Scope revision:"),
        "devspec/work-items/_template/implement.md": ("Changed-work baseline:",),
        "devspec/work-items/_template/review.md": ("Location", "implemented-as-decided", "Changed-work baseline:"),
        "devspec/quickfixes/_template.md": ("last:", "resume:", "next:"),
    }

    def test_templates_carry_the_fields_contracts_require(self) -> None:
        for template, fields in self.REQUIRED_FIELDS.items():
            text = (REPO / template).read_text(encoding="utf-8")
            for field in fields:
                with self.subTest(template=template, field=field):
                    self.assertIn(field, text)

    def test_contract_outputs_have_a_template(self) -> None:
        template_map = (REPO / "devspec/foundation/template-map.md").read_text(encoding="utf-8")
        work_item_templates = {p.name for p in (REPO / "devspec/work-items/_template").glob("*.md")}
        for command in COMMANDS:
            artifacts = list(workflow(command.name).find("outputs"))
            self.assertTrue(artifacts, f"{command.name} declares no output")
            for artifact in artifacts:
                path = artifact.attrib["path"]
                with self.subTest(command=command.name, path=path):
                    name = path.rsplit("/", 1)[-1]
                    if path.startswith("devspec/work-items/"):
                        self.assertIn(name, work_item_templates)
                    elif path.startswith("devspec/foundation/"):
                        self.assertIn(f"`{name}`", template_map)
                    elif path.startswith("devspec/quickfixes/"):
                        self.assertTrue((REPO / "devspec/quickfixes/_template.md").is_file())
                    else:
                        self.assertTrue((REPO / path).is_file(), f"no home for {path}")


if __name__ == "__main__":
    unittest.main()
