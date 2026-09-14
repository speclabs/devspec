from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from devspec.framework import doctor, install_framework


class InstalledContractTests(unittest.TestCase):
    def test_constitution_clarification_architecture_and_batch_contracts_are_installed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            install_framework(target, "all", "existing")
            constitution = (target / "devspec/constitution.md").read_text(encoding="utf-8")
            extract = (target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")
            projectcontext = (target / "devspec/contracts/devspec.projectcontext.md").read_text(encoding="utf-8")
            clarify = (target / "devspec/contracts/devspec.clarify.md").read_text(encoding="utf-8")
            finalize = (target / "devspec/contracts/devspec.finalize.md").read_text(encoding="utf-8")
            tasks = (target / "devspec/contracts/devspec.tasks.md").read_text(encoding="utf-8")
            review = (target / "devspec/contracts/devspec.review.md").read_text(encoding="utf-8")
            diagram = (target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")
            self.assertIn("CP-###", constitution)
            self.assertIn("constitution.md", extract)
            self.assertIn("explicit durable-principle", projectcontext)
            self.assertTrue((target / "devspec/work-items/_template/clarify.md").is_file())
            self.assertIn("exact resume command", clarify)
            self.assertIn("architecture and diagram trace", finalize)
            self.assertIn("architecture traces", tasks)
            self.assertIn("architecture traces", review)
            self.assertIn("explicit process-flow batch request", diagram)
            self.assertEqual([], doctor(target, "all"))


if __name__ == "__main__":
    unittest.main()
