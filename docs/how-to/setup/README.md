# devspec Setup Guides

Use these guides when you are installing `devspec` into a target repository for the first time. They are written for developers who may be new to package managers or command-line setup.

## Which Setup Should I Use?

| Situation | Use this guide |
| --- | --- |
| You want the simplest one-time command. | [uv and uvx](uv.md) |
| Your team already uses Homebrew on macOS or Linux. | [Homebrew](homebrew.md) |
| Your Windows machine uses approved WinGet packages. | [WinGet](winget.md) |
| Package managers are blocked. | [Manual copy](manual-copy.md) |

Install the package manager first when needed:

| Tool | Official install link |
| --- | --- |
| uv | [Install uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Homebrew | [Install Homebrew](https://brew.sh/) |
| WinGet | [Install or use WinGet](https://learn.microsoft.com/windows/package-manager/winget/) |

Recommended default:

```text
uvx devspec init --target . --profile all --repo-state existing
```

## Command-Line Basics

Open a terminal from your target repository when possible. In VS Code, use **Terminal > New Terminal**.

The target repository is the project where you want to install `devspec`. Before running setup commands, go to that folder:

```text
cd D:\code\my-app
```

or on macOS/Linux:

```text
cd /Users/me/code/my-app
```

When a command uses `--target .`, the `.` means "the folder I am currently in."

## Standard Setup Flow

1. Go to your target repository.
2. Install or run `devspec`.
3. Install the framework files.
4. Validate the install.
5. Commit the copied files.

If you are using `uvx`, prefix the `devspec` commands below with `uvx`, for example `uvx devspec doctor --target . --profile all`.

```text
devspec init --target . --profile all --repo-state existing
devspec doctor --target . --profile all
git status
git add .
git commit -m "Install devspec"
```

## What Each Argument Means

| Command or argument | Meaning | Beginner explanation | Common values |
| --- | --- | --- | --- |
| `version` | Print the devspec CLI version. | Use this to confirm the command runs. It does not change files. | `devspec version` |
| `init` | Install devspec files into a repo. | This is the action that copies devspec into your project. | `init` |
| `--target .` | Target repository path. | `.` means "the folder I am currently in." Use this after you `cd` into your repo. | `.`, `D:\code\my-app`, `/Users/me/code/my-app` |
| `--profile all` | Which adapter files to install or check. | `all` installs every supported AI tool integration. Use a smaller profile if your team uses only one tool. Required for `init` and `sync`; optional for `diff` and `doctor`, where it defaults to `all` or the installed manifest profile. | `all`, `core`, `copilot`, `codex`, `cursor`, `claude`, `gemini`, `antigravity` |
| `--repo-state existing` | Whether the target repo already has code. | Required for `init`. Use `existing` for most real projects. Use `new` for a repo that has little or no code yet. | `existing`, `new` |
| `doctor` | Validate a devspec install. | Checks whether required devspec files are present and profiles look complete. | `doctor` |
| `diff` | Compare installed files with the packaged framework. | Shows missing, modified, stale, protected, or profile-mismatched files. It does not write files. | `devspec diff --target .` |
| `sync` | Update framework-owned files. | Applies framework updates while preserving project-owned artifacts. Use `--dry-run` first. | `devspec sync --target . --profile all --dry-run` |
| `--dry-run` | Preview a sync. | Shows what `sync` would change without writing files. Only applies to `sync`. | `--dry-run` |
| `--force` | Overwrite reviewed framework-owned conflicts. | Applies to `init` and `sync`. Use only after reading the conflict output. Do not use casually. | `--force` |

## Common Examples

Check the installed CLI version:

```text
devspec version
```

Install into an existing repository:

```text
devspec init --target . --profile all --repo-state existing
```

Install into a new repository:

```text
devspec init --target . --profile all --repo-state new
```

Validate the install:

```text
devspec doctor --target . --profile all
```

Only GitHub Copilot:

```text
devspec init --target . --profile copilot --repo-state existing
```

Only Codex:

```text
devspec init --target . --profile codex --repo-state existing
```

Only Cursor:

```text
devspec init --target . --profile cursor --repo-state existing
```

Preview an upgrade:

```text
devspec diff --target .
devspec sync --target . --profile all --dry-run
```

Apply an upgrade after reviewing the dry run:

```text
devspec sync --target . --profile all
```

Use an explicit Windows path instead of the current folder:

```text
devspec init --target D:\code\my-app --profile all --repo-state existing
```

Use an explicit macOS/Linux path instead of the current folder:

```text
devspec init --target /Users/me/code/my-app --profile all --repo-state existing
```

## What Success Looks Like

After setup, your target repository should include:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
docs/how-to/
```

If you installed `--profile all`, it should also include adapter folders such as `.claude/`, `.cursor/`, `.gemini/`, and `.agents/`.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The terminal says `devspec` is not found. | Use `uvx devspec ...`, or close and reopen the terminal after installing a persistent command. |
| You are not sure what folder you are in. | Run `pwd` on macOS/Linux or `Get-Location` in PowerShell. |
| You installed into the wrong folder. | Delete only the copied devspec files from that folder, then run the command again from the correct repo. |
| `devspec init` reports conflicts. | Read the conflict list. Use `--force` only after you know the files are framework-owned and safe to replace. |
| Downloads are blocked. | Use [manual copy](manual-copy.md). |
