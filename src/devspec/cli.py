"""Command-line interface for installing, comparing, and synchronizing devspec."""

from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from .framework import (
    PROFILES,
    diff_framework,
    doctor,
    doctor_warnings,
    install_framework,
    manifest_profile,
    migrate_renamed_meta,
    sync_framework,
)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="devspec")
    root.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = root.add_subparsers(dest="command", required=True)
    sub.add_parser("version", help="Print the devspec version (alias for --version)")
    for name in ("init", "doctor", "diff", "sync"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--target", default=".", help="Repository to initialize, compare, synchronize, or validate")
        if name == "sync":
            cmd.add_argument("--profile", choices=PROFILES, required=True)
            cmd.add_argument("--dry-run", action="store_true", help="Show sync changes without writing files")
            cmd.add_argument("--force", action="store_true", help="Overwrite locally modified framework-owned files")
        else:
            cmd.add_argument("--profile", choices=PROFILES, default="all" if name == "init" else None)
        if name == "init":
            cmd.add_argument("--repo-state", choices=("new", "existing"), required=True)
            cmd.add_argument("--force", action="store_true", help="Overwrite changed framework-owned files")
    return root


def _profile(args) -> str:
    return args.profile or manifest_profile(args.target) or "all"


def _report(title: str, values: list[str]) -> None:
    if values:
        print(f"{title}:")
        print("\n".join(f"- {value}" for value in values))


def main(argv: list[str] | None = None) -> int:
    root = parser()
    args = root.parse_args(argv)
    if args.command == "version":
        print(f"devspec {__version__}")
        return 0
    target = Path(args.target).resolve()
    if not target.is_dir():
        root.error(f"target is not a directory: {target}")
    args.target = target
    if args.command == "init":
        try:
            install_framework(target, args.profile, args.repo_state, force=args.force)
        except ValueError as exc:
            print(f"init failed: {exc}")
            return 2
        print(f"Initialized devspec ({args.profile}) in {target}")
        return 0

    profile = _profile(args)
    if args.command == "doctor":
        issues = doctor(target, profile)
        warnings = doctor_warnings(target, profile)
        if issues:
            print("devspec doctor found errors:")
            print("\n".join(f"- {issue}" for issue in issues))
        _report("Warnings", warnings)
        if not issues and not warnings:
            print(f"devspec doctor passed for {target} ({profile})")
        return 1 if issues else 0

    if args.command == "diff":
        report = diff_framework(target, profile)
        for title, key in (("Profile mismatches", "profile"), ("Missing files", "missing"), ("Locally modified files", "modified"), ("Stale packaged files", "stale"), ("Protected project-owned files", "protected"), ("Retained obsolete files", "obsolete")):
            _report(title, report[key])
        if not any(report.values()):
            print("No devspec differences found.")
        return 1 if any(report[key] for key in ("profile", "missing", "modified", "stale", "obsolete")) else 0

    writable, conflicts, skipped, obsolete = sync_framework(target, profile, dry_run=args.dry_run, force=args.force)
    if conflicts:
        _report("Sync conflicts", conflicts)
        _report("Retained obsolete files", obsolete)
        print("No files were written. Run with --dry-run first, then use --force only for reviewed framework-owned files.")
        return 1
    renamed = migrate_renamed_meta(target, dry_run=args.dry_run)
    if args.dry_run:
        print(f"Dry run for devspec ({profile}) in {target}")
        _report("Files that would be written", writable)
        _report("Work-item values that would be renamed", renamed)
    else:
        print(f"Synchronized devspec ({profile}) in {target}")
        _report("Files written", writable)
        _report("Work-item values renamed", renamed)
    _report("Skipped files", skipped)
    _report("Retained obsolete files", obsolete)
    return 0
