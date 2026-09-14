from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from devspec import __version__


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


class ReleaseMetadataTests(unittest.TestCase):
    def test_pyproject_reads_the_single_cli_version(self) -> None:
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('dynamic = ["version"]', pyproject)
        self.assertIn('version = {attr = "devspec.__version__"}', pyproject)
        self.assertNotIn('\nversion = "', pyproject)

    def test_release_tag_must_match_package_version(self) -> None:
        command = [sys.executable, str(ROOT / "scripts" / "verify_release_version.py")]
        matching = subprocess.run([*command, "--tag", f"v{__version__}"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, matching.returncode, matching.stderr)
        mismatched = subprocess.run([*command, "--tag", "v9.9.9"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(2, mismatched.returncode)
        self.assertIn("does not match package version", mismatched.stderr)

    def test_release_templates_are_parameterized(self) -> None:
        winget = ROOT / "packaging" / "winget"
        for name in ("SpecLabs.Devspec.yaml", "SpecLabs.Devspec.installer.yaml", "SpecLabs.Devspec.locale.en-US.yaml"):
            with self.subTest(manifest=name):
                text = (winget / name).read_text(encoding="utf-8")
                self.assertIn("PackageIdentifier: SpecLabs.Devspec", text)
                self.assertIn("PackageVersion: REPLACE_WITH_VERSION", text)
                self.assertIn("ManifestVersion:", text)
        installer = (winget / "SpecLabs.Devspec.installer.yaml").read_text(encoding="utf-8")
        homebrew = (ROOT / "packaging" / "homebrew" / "devspec.rb").read_text(encoding="utf-8")
        self.assertIn("REPLACE_WITH_RELEASE_URL", installer)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", installer)
        self.assertIn("REPLACE_WITH_VERSION", homebrew)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", homebrew)
        self.assertIn('resource "setuptools"', homebrew, "Homebrew builds without isolation and needs the build backend")

    def test_release_workflows_generate_and_publish_artifacts(self) -> None:
        python_publish = (WORKFLOWS / "python-package-publish.yml").read_text(encoding="utf-8")
        winget_publish = (WORKFLOWS / "winget-package-publish.yml").read_text(encoding="utf-8")
        homebrew_publish = (WORKFLOWS / "homebrew-package-publish.yml").read_text(encoding="utf-8")
        for workflow in (python_publish, winget_publish, homebrew_publish):
            self.assertIn("verify_release_version.py", workflow)
            self.assertNotIn("devspec-lite", workflow)
        self.assertIn("devspec-python-package-checksums.txt", python_publish)
        self.assertIn("uv publish dist/*.tar.gz dist/*.whl", python_publish)
        self.assertIn("Get-FileHash", winget_publish)
        self.assertIn("devspec.exe.sha256", winget_publish)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", winget_publish)
        self.assertIn("curl -fsSL", homebrew_publish)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", homebrew_publish)
        # A dispatch input interpolated straight into a run script is a script-injection path.
        self.assertNotIn("${{ inputs.version }}\"", homebrew_publish)

    def test_pypi_publish_is_limited_to_release_tags(self) -> None:
        python_publish = (WORKFLOWS / "python-package-publish.yml").read_text(encoding="utf-8")
        step = python_publish[python_publish.index("- name: Publish Python package to PyPI"):]
        self.assertIn("if: startsWith(github.ref, 'refs/tags/v')", step.split("\n", 2)[1])


if __name__ == "__main__":
    unittest.main()
