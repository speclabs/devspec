from __future__ import annotations

import re
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree

from devspec.cli import main
from devspec.definitions import COMMANDS
from devspec.framework import PROFILES, doctor, install_framework, xml_block


class FrameworkTests(unittest.TestCase):
    def test_version_flag(self) -> None:
        with self.assertRaises(SystemExit) as result:
            main(["--version"])
        self.assertEqual(0, result.exception.code)

    def test_init_all_and_doctor(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            self.assertEqual(0, main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"]))
            self.assertEqual([], doctor(target, "all"))
            self.assertEqual(0, main(["doctor", "--target", str(target), "--profile", "all"]))
            self.assertEqual(len(COMMANDS), len(list((target / "devspec/contracts").glob("*.md"))))
            self.assertTrue((target / ".github/agents/devspec.quickfix.agent.md").is_file())
            self.assertTrue((target / ".claude/skills/devspec-refine/SKILL.md").is_file())
            self.assertIn("devspec.extract", (target / "devspec/foundation/repository-state.md").read_text(encoding="utf-8"))

    def test_init_and_doctor_every_profile(self) -> None:
        for profile in PROFILES:
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as raw:
                target = Path(raw)
                install_framework(target, profile, "existing")
                self.assertEqual([], doctor(target, profile))

    def test_doctor_checks_required_xml_tags_and_templates(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            install_framework(target, "codex", "existing")
            (target / "devspec/protocols/run.xml").write_text('<protocol id="run" />\n', encoding="utf-8")
            (target / "devspec/work-items/_template/tasks.md").unlink()
            issues = doctor(target, "codex")
            self.assertTrue(any("missing protocol tags" in issue for issue in issues))
            self.assertIn("missing: devspec/work-items/_template/tasks.md", [issue.replace("\\", "/") for issue in issues])

    def test_ask_protocol_requires_interactive_choices(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            root = ElementTree.fromstring((target / "devspec/protocols/ask.xml").read_text(encoding="utf-8"))
            interaction = root.find("interaction")
            self.assertIsNotNone(interaction)
            self.assertEqual("interactive", interaction.attrib["mode"])
            self.assertEqual("true", interaction.find("recommendation").attrib["required"])
            self.assertEqual("true", interaction.find("recommendation").attrib["justification-required"])
            self.assertEqual("true", interaction.find("custom-answer").attrib["required"])
            self.assertIn("every applicable unresolved material question", root.findtext("discovery"))
            self.assertIn("exactly one unanswered material question", root.findtext("sequence"))
            self.assertIn("every material question is answered or skipped", root.findtext("completion"))
            self.assertIn("Skip an invalid or inapplicable material question", root.findtext("completion"))
            self.assertEqual("devspec/foundation/decisions.md", root.findtext("decision-records/foundation"))
            work = ElementTree.fromstring((target / "devspec/protocols/work.xml").read_text(encoding="utf-8"))
            self.assertIn("including meta.md and decisions.md", work.findtext("initialize"))
            self.assertIn("template-map.md", work.findtext("initialize"))
            run = ElementTree.fromstring((target / "devspec/protocols/run.xml").read_text(encoding="utf-8"))
            self.assertEqual("devspec/foundation/decisions.md", run.findtext("state-records/foundation"))
            repo_access = ElementTree.fromstring((target / "devspec/protocols/repo-access.xml").read_text(encoding="utf-8"))
            self.assertIn("Never validate a reference-only, edit, release-coordination, or unavailable repository", repo_access.findtext("respect"))
            self.assertTrue((target / "devspec/foundation/template-map.md").is_file())
            self.assertTrue((target / "devspec/foundation/_template/decisions.md").is_file())
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertFalse((target / ".github").exists())

    def test_reusable_decision_traceability_is_installed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            decisions = (target / "devspec/work-items/_template/decisions.md").read_text(encoding="utf-8")
            workflow_rules = (target / "devspec/foundation/_template/workflow-rules.md").read_text(encoding="utf-8")
            engineering_rules = (target / "devspec/foundation/_template/rules.md").read_text(encoding="utf-8")
            tasks = (target / "devspec/work-items/_template/tasks.md").read_text(encoding="utf-8")
            implementation = (target / "devspec/work-items/_template/implement.md").read_text(encoding="utf-8")
            review = (target / "devspec/work-items/_template/review.md").read_text(encoding="utf-8")
            finalize = (target / "devspec/contracts/devspec.finalize.md").read_text(encoding="utf-8")
            implement_contract = (target / "devspec/contracts/devspec.implement.md").read_text(encoding="utf-8")
            review_contract = (target / "devspec/contracts/devspec.review.md").read_text(encoding="utf-8")
            story = (target / "devspec/contracts/devspec.story.md").read_text(encoding="utf-8")
            self.assertIn("Applicability", decisions)
            self.assertIn("Canonical rule link", decisions)
            self.assertIn("Rule ID", workflow_rules)
            self.assertIn("Source decision", workflow_rules)
            self.assertIn("Rule ID", engineering_rules)
            self.assertIn("Decision or rule IDs", tasks)
            self.assertIn("Decision or rule IDs", implementation)
            self.assertIn("Decision and Rule Verification", review)
            self.assertIn("Promote a reusable business or validation decision", finalize)
            self.assertIn("canonical rule ID", implement_contract)
            self.assertIn("implemented-as-decided", review_contract)
            self.assertIn("do not scan unrelated historical work-item decisions", story)
    def test_security_foundation_and_confirmed_exception_path_are_installed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            rules = (target / "devspec/foundation/_template/rules.md").read_text(encoding="utf-8")
            finalize_template = (target / "devspec/work-items/_template/finalize.md").read_text(encoding="utf-8")
            implementation_template = (target / "devspec/work-items/_template/implement.md").read_text(encoding="utf-8")
            review_template = (target / "devspec/work-items/_template/review.md").read_text(encoding="utf-8")
            rules_contract = (target / "devspec/contracts/devspec.rules.md").read_text(encoding="utf-8")
            extract_contract = (target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")
            finalize_contract = (target / "devspec/contracts/devspec.finalize.md").read_text(encoding="utf-8")
            implement_contract = (target / "devspec/contracts/devspec.implement.md").read_text(encoding="utf-8")
            review_contract = (target / "devspec/contracts/devspec.review.md").read_text(encoding="utf-8")
            security_protocol = (target / "devspec/protocols/security.xml").read_text(encoding="utf-8")
            self.assertEqual(1, rules.count("OWASP Top 10:2025 Baseline"))
            self.assertIn("A01:2025 Broken Access Control", rules)
            self.assertIn("A10:2025 Mishandling of Exceptional Conditions", rules)
            self.assertIn("Foundation Traceability", finalize_template)
            self.assertIn("OWASP Security Assessment", finalize_template)
            self.assertIn("Security Evidence and Proposed Exceptions", implementation_template)
            self.assertIn("Developer confirmation", implementation_template)
            self.assertIn("Security Verification", review_template)
            self.assertIn("Reviewer confirmation", review_template)
            # The security protocol owns the baseline, exception, and gate; the contracts load it.
            self.assertIn("OWASP Top 10:2025", security_protocol)
            self.assertIn("one material confirmation question", security_protocol)
            self.assertIn("known unresolved vulnerability", security_protocol)
            for contract in (rules_contract, extract_contract, finalize_contract, implement_contract, review_contract):
                self.assertIn('<protocol ref="security" />', contract)
            self.assertIn("internal-only", security_protocol)
            self.assertIn("foundation trace", finalize_contract)
    def test_contract_xml_and_quickfix_routing_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "copilot", "--repo-state", "existing"])
            quickfix = (target / "devspec/contracts/devspec.quickfix.md").read_text(encoding="utf-8")
            self.assertIn("Route public API contracts", quickfix)
            self.assertIn("database schema or migration", quickfix)
            self.assertIn("<rules>", quickfix)
            self.assertIn('<protocol ref="ask" />', quickfix)
            self.assertIn("devspec/contracts/devspec.quickfix.md", (target / ".github/prompts/devspec.quickfix.prompt.md").read_text(encoding="utf-8"))
            self.assertEqual([], doctor(target, "copilot"))

    def test_extract_completes_existing_system_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"])
            extract = ElementTree.fromstring(xml_block((target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")))
            refs = {protocol.attrib["ref"] for protocol in extract.find("protocols")}
            self.assertTrue({"ask", "run", "work", "repo-access"}.issubset(refs))
            outputs = {artifact.attrib["path"] for artifact in extract.find("outputs")}
            self.assertIn("devspec/foundation/workflows.md", outputs)
            self.assertIn("devspec/foundation/workflow-rules.md", outputs)
            self.assertIn("devspec/architecture/artifact-queue.md", outputs)
            self.assertTrue((target / "devspec/foundation/_template/technical-baseline.md").is_file())
            self.assertTrue((target / "devspec/foundation/_template/extraction-coverage.md").is_file())
            diagram_types = (target / "devspec/architecture/_template/diagram-types.md").read_text(encoding="utf-8")
            self.assertIn("Infrastructure topology", diagram_types)
            self.assertIn("Application landscape", diagram_types)
            structure = (target / "devspec/contracts/devspec.codebase-structure.md").read_text(encoding="utf-8")
            structure_template = (target / "devspec/foundation/_template/codebase-structure.md").read_text(encoding="utf-8")
            self.assertIn("record an observed repository layout", (target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8"))
            self.assertIn("developer-provided layout tree", structure)
            self.assertIn("## Repository Layouts", structure_template)
            self.assertIn("Origin:** Observed | Developer-defined", structure_template)

    def test_extract_prepares_diagrams_and_requests_generation_confirmation(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            extract = (target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")
            diagram = (target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")
            how_to = (Path(__file__).resolve().parents[1] / "docs/how-to.md").read_text(encoding="utf-8")
            self.assertIn("Do you want me to generate all the possible diagrams?", extract)
            self.assertIn("Yes — generate all listed diagrams", extract)
            self.assertIn("No — prepare the list only", extract)
            self.assertIn("Choose diagrams — enter the IDs or subjects to generate", extract)
            self.assertIn("/devspec.diagram &lt;DIA-ID-or-subject&gt;", extract)
            self.assertIn("do not generate an SVG", extract)
            self.assertIn("Accept a stable queued `DIA-###` ID", diagram)
            self.assertIn("/devspec.diagram DIA-002", how_to)

    def test_coding_standard_examples_are_extracted_and_can_be_developer_defined(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            extract = (target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")
            standards = (target / "devspec/contracts/devspec.coding-standards.md").read_text(encoding="utf-8")
            template = (target / "devspec/foundation/_template/coding-standards.md").read_text(encoding="utf-8")
            implement = (target / "devspec/contracts/devspec.implement.md").read_text(encoding="utf-8")
            self.assertIn("stable `CS-###` ID", extract)
            self.assertIn("developer-defined custom standards with followable numbered examples", standards)
            self.assertIn("Mark it developer-defined rather than observed", standards)
            self.assertIn("Developer-defined", template)
            self.assertIn("## Standards Examples", template)
            self.assertIn("Standard ID", template)
            self.assertIn("EX-###", template)
            self.assertIn("stable `CS-###` ID", standards)
            self.assertIn("Preserve existing `CS-###` and `EX-###` IDs", standards)
            self.assertIn("linked `EX-###` entries", standards)
            self.assertIn("## Standards Examples", extract)
            self.assertIn("coding standards and their follow examples", implement)
    def test_command_scopes_and_closure_are_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            for command in ("projectcontext", "techstack", "codebase-structure", "coding-standards", "rules"):
                contract = (target / f"devspec/contracts/devspec.{command}.md").read_text(encoding="utf-8")
                self.assertIn("new-repository foundation authoring", contract)
                self.assertIn("devspec.extract, not this command", contract)
            diagram = ElementTree.fromstring(xml_block((target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")))
            diagram_refs = {protocol.attrib["ref"] for protocol in diagram.find("protocols")}
            self.assertIn("repo-access", diagram_refs)
            self.assertIn("targeted diagram", diagram.findtext("scope"))
            quickfix = (target / "devspec/contracts/devspec.quickfix.md").read_text(encoding="utf-8")
            self.assertIn("user-defined bounded scope", quickfix)
            self.assertIn("Never assign the number automatically", quickfix)
            change_request = (target / "devspec/contracts/devspec.changerequest.md").read_text(encoding="utf-8")
            self.assertIn("material classification question", change_request)
            review = (target / "devspec/contracts/devspec.review.md").read_text(encoding="utf-8")
            review_template = (target / "devspec/work-items/_template/review.md").read_text(encoding="utf-8")
            self.assertIn("accepted, rework-required, or blocked", review)
            self.assertIn("Outcome: accepted | rework-required | blocked", review_template)
            self.assertIn("Next action:", review_template)
    def test_installs_complete_compact_artifact_structure(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "new"])
            self.assertTrue((target / "devspec/README.md").is_file())
            self.assertTrue((target / "devspec/glossary.md").is_file())
            self.assertTrue((target / "devspec/architecture/_template/artifact-queue.md").is_file())
            self.assertTrue((target / "devspec/architecture/artifact-queue.md").is_file())
            sample = (target / "devspec/architecture/_template/diagram-sample.md").read_text(encoding="utf-8")
            self.assertIn("DIA-001", sample)
            self.assertTrue((target / "devspec/architecture/_template/diagram-sample.svg").is_file())
            sample_svg = ElementTree.parse(target / "devspec/architecture/_template/diagram-sample.svg").getroot()
            self.assertIsNotNone(sample_svg.find("{http://www.w3.org/2000/svg}title"))
            self.assertIsNotNone(sample_svg.find("{http://www.w3.org/2000/svg}desc"))
            self.assertTrue((target / "devspec/foundation/_template/exploration-state.md").is_file())
            meta = (target / "devspec/work-items/_template/meta.md").read_text(encoding="utf-8")
            self.assertIn("stage:", meta)
            self.assertIn("run:", meta)
            self.assertIn("last:", meta)

    def test_diagram_contract_preserves_traceability_and_svg_quality(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            diagram = (target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")
            self.assertIn("non-duplicate diagrams", diagram)
            self.assertIn("index completed output in the overview", diagram)
            self.assertIn("title and description", diagram)
            self.assertIn("validate its XML", diagram)
            self.assertIn("Mermaid or HTML", diagram)
            self.assertIn("motion=none|explain", diagram)
            self.assertIn("svg; motion=explain", diagram)
            self.assertTrue((target / "devspec/architecture/artifact-queue.md").is_file())
            self.assertTrue((target / "devspec/architecture/overview.md").is_file())

    def test_motion_diagram_sample_is_accessible_finite_and_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            sample = target / "devspec/architecture/_template/diagram-motion-sample.svg"
            root = ElementTree.parse(sample).getroot()
            namespace = "{http://www.w3.org/2000/svg}"
            self.assertEqual("0 0 1600 900", root.attrib["viewBox"])
            self.assertEqual("img", root.attrib["role"])
            self.assertNotIn("width", root.attrib)
            self.assertNotIn("height", root.attrib)
            self.assertIsNotNone(root.find(f"{namespace}title"))
            self.assertIsNotNone(root.find(f"{namespace}desc"))
            self.assertEqual([], root.findall(f".//{namespace}script"))
            self.assertEqual([], root.findall(f".//{namespace}foreignObject"))

            serialized = ElementTree.tostring(root, encoding="unicode")
            ids = {element.attrib["id"] for element in root.iter() if "id" in element.attrib}
            references = set(re.findall(r"url\(#([^)]+)\)", serialized))
            references.update(
                value[1:]
                for element in root.iter()
                for key, value in element.attrib.items()
                if key.endswith("href") and value.startswith("#")
            )
            self.assertFalse(references - ids)
            self.assertNotIn("http://", serialized.replace("http://www.w3.org/2000/svg", ""))
            self.assertNotIn("https://", serialized)
            self.assertNotRegex(serialized, r"\[[A-Z][A-Z0-9_ /-]*\]")

            style = "".join(root.find(f".//{namespace}style").itertext())
            self.assertIn("prefers-reduced-motion: reduce", style)
            self.assertNotIn("infinite", style)
            self.assertIn("animation: none !important", style)
            self.assertIn("stroke-dashoffset: 0 !important", style)
            self.assertTrue(any(path.attrib.get("pathLength") == "1" for path in root.findall(f".//{namespace}path")))

    def test_family_specific_diagram_templates_are_installed_and_well_formed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            template_root = target / "devspec/architecture/_template"
            expected = (
                "architecture-diagram.svg",
                "application-landscape-diagram.svg",
                "infrastructure-topology-diagram.svg",
                "process-flow-diagram.svg",
                "sequence-diagram.svg",
                "state-lifecycle-diagram.svg",
                "domain-model-diagram.svg",
                "journey-map-diagram.svg",
                "timeline-plan-diagram.svg",
                "quadrant-analysis-diagram.svg",
                "mindmap-diagram.svg",
            )
            for name in expected:
                with self.subTest(name=name):
                    root = ElementTree.parse(template_root / name).getroot()
                    self.assertEqual("0 0 1600 900", root.attrib["viewBox"])
                    self.assertIsNotNone(root.find("{http://www.w3.org/2000/svg}title"))
                    self.assertIsNotNone(root.find("{http://www.w3.org/2000/svg}desc"))
            diagram = (target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")
            self.assertIn("Start each SVG from the matching family-specific template", diagram)
            self.assertIn("connectors behind cards", diagram)
            self.assertIn("Anchor every connector to a shape edge at both ends", diagram)
            types = (target / "devspec/architecture/_template/diagram-types.md").read_text(encoding="utf-8")
            for name in expected:
                with self.subTest(mapped=name):
                    self.assertIn(f"`{name}`", types)

    def test_diagram_templates_have_no_dangling_marker_references(self) -> None:
        """A marker-end pointing at a missing id renders a connector with no arrowhead."""
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            namespace = "{http://www.w3.org/2000/svg}"
            for path in sorted((target / "devspec/architecture/_template").glob("*.svg")):
                with self.subTest(template=path.name):
                    root = ElementTree.parse(path).getroot()
                    defined = {marker.attrib.get("id") for marker in root.iter(f"{namespace}marker")}
                    referenced = set()
                    for element in root.iter():
                        for attribute in ("marker-end", "marker-start", "filter", "fill", "stroke"):
                            value = element.attrib.get(attribute, "")
                            if value.startswith("url(#"):
                                referenced.add(value[5:-1])
                    self.assertTrue(referenced <= defined | {node.attrib.get("id") for node in root.iter()},
                                    f"{path.name} references an undefined id")
                    serialized = ElementTree.tostring(root, encoding="unicode")
                    self.assertNotIn("<script", serialized)
                    self.assertNotIn("foreignObject", serialized)
                    self.assertNotIn("<iframe", serialized)

    def test_init_refuses_changed_managed_file(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            contract = target / "devspec/contracts/devspec.story.md"
            contract.write_text("user change", encoding="utf-8")
            self.assertEqual(2, main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"]))

    def test_doctor_reports_missing_contract(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "gemini", "--repo-state", "new"])
            (target / "devspec/contracts/devspec.rules.md").unlink()
            issues = doctor(target, "gemini")
            self.assertTrue(any("devspec.rules.md" in issue for issue in issues))

    def test_doctor_rejects_wrapper_logic_or_missing_reference(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "claude", "--repo-state", "new"])
            wrapper = target / ".claude/skills/devspec-story/SKILL.md"
            wrapper.write_text("<workflow />", encoding="utf-8")
            issues = doctor(target, "claude")
            self.assertTrue(any("does not reference contract" in issue for issue in issues))
            self.assertTrue(any("duplicates workflow logic" in issue for issue in issues))


    def test_sync_renames_work_item_values_a_command_rename_left_behind(self) -> None:
        # Work items created before devspec.grooming became devspec.refine still name the old command.
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            meta = target / "devspec/work-items/260101-01-export/meta.md"
            meta.parent.mkdir(parents=True)
            legacy = "---\nstage: grooming\nrun: active\nresume: none\nnext: devspec.grooming\n---\n"
            meta.write_text(legacy, encoding="utf-8")
            self.assertTrue(any("stage: grooming -> refinement" in issue for issue in doctor(target, "codex")))
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "codex", "--dry-run"]))
            self.assertEqual(legacy, meta.read_text(encoding="utf-8"))
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "codex"]))
            self.assertEqual(legacy.replace("stage: grooming", "stage: refinement").replace("devspec.grooming", "devspec.refine"), meta.read_text(encoding="utf-8"))
            self.assertEqual([], doctor(target, "codex"))

    def test_lifecycle_contracts_are_complete_and_routable(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"])
            self.assertTrue((target / "devspec/lifecycle.md").is_file())
            required = {"entry", "outputs", "transitions", "closure"}
            valid_next = {f"devspec.{command.name}" for command in COMMANDS} | {"none", "return-to-caller", "resume-origin"}
            for command in COMMANDS:
                contract = (target / f"devspec/contracts/devspec.{command.name}.md").read_text(encoding="utf-8")
                workflow = ElementTree.fromstring(xml_block(contract))
                self.assertFalse(required - {child.tag for child in workflow})
                transitions = workflow.find("transitions")
                self.assertIsNotNone(transitions)
                for transition in transitions or ():
                    self.assertIn(transition.attrib["next"], valid_next)
                    self.assertIn(transition.attrib["run"], {"active", "blocked", "complete"})

    def test_doctor_rejects_invalid_lifecycle_transition(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            contract = target / "devspec/contracts/devspec.rules.md"
            text = contract.read_text(encoding="utf-8").replace('next="devspec.story"', 'next="devspec.missing"')
            contract.write_text(text, encoding="utf-8")
            issues = doctor(target, "codex")
            self.assertTrue(any("invalid lifecycle transition" in issue for issue in issues))

    def test_current_work_item_protocol_and_optional_ids_are_installed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            protocol = ElementTree.fromstring((target / "devspec/protocols/current-work-item.xml").read_text(encoding="utf-8"))
            self.assertIn("git rev-parse --git-path devspec/current-work-item.json", protocol.findtext("location"))
            self.assertIn("selection source", protocol.findtext("record"))
            self.assertIn("devspec.clarify", protocol.findtext("continuation"))
            self.assertFalse((target / "devspec/work-items/current.md").exists())
            for command in ("story", "refine", "finalize", "tasks", "implement", "review", "clarify", "changerequest"):
                with self.subTest(command=command):
                    contract = (target / f"devspec/contracts/devspec.{command}.md").read_text(encoding="utf-8")
                    workflow = ElementTree.fromstring(xml_block(contract))
                    refs = {item.attrib["ref"] for item in workflow.find("protocols")}
                    self.assertIn("current-work-item", refs)
                    if command != "story":
                        self.assertIn(f"/devspec.{command} [work-item-id]", contract)
            how_to = (Path(__file__).resolve().parents[1] / "docs/how-to.md").read_text(encoding="utf-8")
            self.assertIn("Continue current work without an ID", how_to)
            self.assertIn("selected `meta.md` next action", how_to)
            self.assertIn("post-finalization route", how_to)
            # Both the legacy path and the path a real violation takes today.
            for forbidden in ("devspec/work-items/current.md", "devspec/current-work-item.json"):
                tracked_context = target / forbidden
                tracked_context.parent.mkdir(parents=True, exist_ok=True)
                tracked_context.write_text("current: STORY-001\n", encoding="utf-8")
                issues = doctor(target, "all")
                self.assertTrue(any(f"tracked current-work-item artifact is not allowed: {forbidden}" in issue for issue in issues))
                tracked_context.unlink()

if __name__ == "__main__":
    unittest.main()
