"""Verify that a release tag matches devspec's single package version."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "src" / "devspec" / "__init__.py"
VERSION_PATTERN = re.compile(r'^__version__\s*=\s*["\'](?P<version>[^"\']+)["\']\s*$', re.MULTILINE)
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:[.-][0-9A-Za-z.-]+)?$")


def package_version() -> str:
    match = VERSION_PATTERN.search(VERSION_FILE.read_text(encoding="utf-8"))
    if match is None:
        raise ValueError(f"Unable to read __version__ from {VERSION_FILE}")
    return match.group("version")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True, help="Release tag, for example v0.1.0")
    args = parser.parse_args()

    tag_version = args.tag.removeprefix("v")
    expected = package_version()
    if not SEMVER_PATTERN.fullmatch(expected):
        print(f"Invalid package version: {expected}", file=sys.stderr)
        return 2
    if tag_version != expected:
        print(f"Release tag {args.tag!r} does not match package version {expected!r}", file=sys.stderr)
        return 2
    print(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())