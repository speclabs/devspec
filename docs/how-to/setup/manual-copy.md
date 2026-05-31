# Manual Copy Setup

Use manual copy only when command-line installers are blocked. It is supported, but the CLI paths are safer because they can validate files and detect conflicts.

## Before You Start

- Download or open a trusted `devspec` release.
- Open the target repository in your file explorer or editor.
- Do not overwrite the target repository's root `README.md`.

## Open A Terminal

Manual copy can be done with a file explorer. A terminal is still useful for validation with `git status`.

## Go To Your Target Repository

Windows PowerShell:

```text
cd D:\code\my-app
```

macOS/Linux:

```text
cd /Users/me/code/my-app
```

## Copy devspec Files

Copy these core files and folders into the target repository root:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
docs/how-to/
```

Then copy only the adapter files your team uses:

| Tool | Additional files |
| --- | --- |
| GitHub Copilot | `.github/skills/` |
| Claude Code | `.claude/` |
| OpenAI Codex | No extra files beyond `AGENTS.md` |
| Cursor | `.cursor/` |
| Gemini CLI | `GEMINI.md`, `.gemini/` |
| Google Antigravity | `.agents/` |

Do not copy this framework repository's root `README.md` over your target project's README.

## Validate The Install

If the CLI is available, run:

```text
devspec doctor --target . --profile all
```

If the CLI is not available, visually confirm these exist:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
```

Then check Git sees the copied files:

```text
git status
```

## Commit The Copied Framework Files

```text
git add .
git commit -m "Install devspec"
```

## Common Examples

Manual copy for all supported tools:

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
docs/how-to/
```

Manual copy for GitHub Copilot only:

```text
devspec/
.github/prompts/
.github/agents/
.github/skills/
AGENTS.md
docs/how-to/
```

Manual copy for Codex only:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
docs/how-to/
```

Manual copy for Cursor only:

```text
devspec/
.github/prompts/
.github/agents/
.cursor/
AGENTS.md
docs/how-to/
```

## Argument Reference

Manual copy does not use CLI arguments. If you later use the CLI, these are the common arguments:

| Argument | Meaning | Beginner explanation |
| --- | --- | --- |
| `version` | Print the devspec CLI version. | Use this to confirm the command runs if the CLI becomes available later. |
| `init` | Install devspec files. | Copies framework files into your repo. |
| `--target .` | Target repo folder. | `.` means the folder your terminal is currently in. |
| `--profile all` | Install or check profile. | `all` installs every supported adapter. Required for `init` and `sync`; optional for `diff` and `doctor`. |
| `--repo-state existing` | Repo type. | Required for `init`. Use `existing` for most projects and `new` for empty or early repos. |
| `doctor` | Validate install. | Checks that expected files exist. |
| `diff` | Compare files. | Shows missing, modified, stale, protected, or profile-mismatched files without writing changes. |
| `sync` | Update framework-owned files. | Applies framework updates while preserving project-owned artifacts. |
| `--dry-run` | Preview a sync. | Shows what `sync` would change without writing files. |
| `--force` | Overwrite reviewed conflicts. | Applies to `init` and `sync`; use only after reading conflict output. |

## Troubleshooting

| Problem | What to try |
| --- | --- |
| You are not sure what to copy. | Start with the core list, then add only the row for your AI coding tool. |
| You accidentally copied the framework README over your project README. | Restore the project README from Git, then copy only `docs/how-to/`. |
| Git shows too many unrelated files. | Check that you copied only the listed files and did not include `.git/`, `.venv/`, `dist/`, or build output. |
| The AI tool does not recognize commands. | Use the command as chat intent, for example `Run /devspec.extract for this repository.` |
