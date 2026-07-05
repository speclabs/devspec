# Manual Copy Setup

Use manual copy only when package managers and command-line installers are blocked. Prefer CLI setup when possible because it can validate files, detect conflicts, and report profile mismatches.

For command-line setup, argument explanations, and upgrade examples, see [Setup Guides](README.md).

## Before You Start

- Download or open a trusted `devspec` release.
- Open the target repository in your file explorer or editor.
- Do not overwrite the target repository's root `README.md`.
- Do not copy `.github/workflows/`; those workflows publish and validate the `devspec` framework itself, not target repositories.

## Choose Files By Tool

Copy these core files first:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
```

Then add only the files for the AI coding tools your team uses:

| Tool | Add these files |
| --- | --- |
| GitHub Copilot | `.github/skills/` |
| Claude Code | `.claude/` |
| OpenAI Codex | No extra files; use core only |
| Cursor | `.cursor/` |
| Gemini CLI | `GEMINI.md`, `.gemini/` |
| Google Antigravity | `.agents/` |

For one AI coding tool, copy the core files plus that tool's row. Codex uses the core files only.

For all supported tools, copy:

```text
devspec/
.github/prompts/
.github/agents/
.github/skills/
.claude/
.cursor/
.gemini/
.agents/
AGENTS.md
GEMINI.md
```

## Copy Safely

Copy the selected files and folders into the target repository root. Do not copy `.git/`, `.venv/`, `dist/`, or build output.

If your terminal opens somewhere else, go to the target repository before validation.

Windows PowerShell:

```text
cd D:\code\my-app
```

macOS/Linux:

```text
cd /Users/me/code/my-app
```

## Validate The Install

Visually confirm the files from [Choose Files By Tool](#choose-files-by-tool) exist, then check Git sees the copied files:

```text
git status
```

## Commit The Copied Framework Files

```text
git add .
git commit -m "Install devspec"
```

## Troubleshooting

| Problem | What to try |
| --- | --- |
| You are not sure what to copy. | Start with the core list, then add only the row for your AI coding tool. |
| You copied the framework README over your project README. | Restore the project README from Git, then copy only the framework files listed above. |
| Git shows too many unrelated files. | Check that you copied only the listed files and did not include `.git/`, `.venv/`, `dist/`, or build output. |
| The AI tool does not recognize commands. | Use the command as chat intent, for example `Run /devspec.extract for this repository.` |
