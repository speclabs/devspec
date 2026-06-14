# Setup With uv and uvx

Use this guide when you want the simplest command-line setup. `uvx devspec ...` downloads and runs `devspec` for one command without permanently installing the `devspec` command.

## Before You Start

- You need `uv` installed. Use the official guide: [Install uv](https://docs.astral.sh/uv/getting-started/installation/).
- Open the target repository in VS Code or your preferred terminal.
- Use this path when package managers are allowed but you do not want to change shared PATH folders.

## Open A Terminal

In VS Code, use **Terminal > New Terminal**.

## Go To Your Target Repository

Windows PowerShell:

```text
cd D:\code\my-app
```

macOS/Linux:

```text
cd /Users/me/code/my-app
```

## Install Or Run devspec

One-time setup with `uvx`:

```text
uvx devspec init --target . --profile all --repo-state existing
```

Persistent local install:

```text
uv tool install devspec
devspec init --target . --profile all --repo-state existing
```

Use `--repo-state new` for a repo that has little or no code yet:

```text
uvx devspec init --target . --profile all --repo-state new
```

## Validate The Install

If you used `uvx`:

```text
uvx devspec doctor --target . --profile all
```

If you installed the persistent command:

```text
devspec doctor --target . --profile all
```

## Commit The Copied Framework Files

```text
git status
git add .
git commit -m "Install devspec"
```

## Common Examples

Check the CLI version:

```text
uvx devspec version
```

Install all adapters into an existing repo:

```text
uvx devspec init --target . --profile all --repo-state existing
```

Install only Copilot support:

```text
uvx devspec init --target . --profile copilot --repo-state existing
```

Install only Codex support:

```text
uvx devspec init --target . --profile codex --repo-state existing
```

Install only Cursor support:

```text
uvx devspec init --target . --profile cursor --repo-state existing
```

Preview an upgrade:

```text
uvx devspec diff --target .
uvx devspec sync --target . --profile all --dry-run
```

Use an explicit target path:

```text
uvx devspec init --target D:\code\my-app --profile all --repo-state existing
uvx devspec init --target /Users/me/code/my-app --profile all --repo-state existing
```

## Argument Reference

| Argument | Meaning | Beginner explanation |
| --- | --- | --- |
| `uvx devspec` | Run devspec once through uv. | Downloads and runs the CLI for this command. |
| `uv tool install devspec` | Install devspec as a user-local tool. | Makes the `devspec` command available for later terminal sessions when PATH is configured. |
| `version` | Print the devspec CLI version. | Use this to confirm the command runs. It does not change files. |
| `init` | Install devspec files. | Copies framework files into your repo. |
| `--target .` | Target repo folder. | `.` means the folder your terminal is currently in. |
| `--profile all` | Install or check profile. | `all` installs every supported adapter. Required for `init` and `sync`; optional for `diff` and `doctor`, where omission uses the installed manifest profile or falls back to `all`. |
| `--repo-state existing` | Repo type. | Required for `init`. Use `existing` for most projects and `new` for empty or early repos. |
| `doctor` | Validate install. | Checks that the expected files exist. |
| `diff` | Compare files. | Shows installed/package version context, then checksum-based missing, modified, stale, protected, or profile-mismatched files without writing changes. |
| `sync` | Update framework-owned files. | Applies framework updates using checksum comparisons while preserving project-owned artifacts. |
| `--dry-run` | Preview only. | Shows what `sync` would do without changing files. |
| `--force` | Overwrite reviewed conflicts. | Applies to `init` and `sync`; use only after reading conflict output. |

## Troubleshooting

| Problem | What to try |
| --- | --- |
| `uv` is not found. | Install `uv`, or use [manual copy](manual-copy.md) if installs are blocked. |
| `uvx` downloads are blocked. | Ask your team if package-index access is restricted, or use [manual copy](manual-copy.md). |
| The command runs in the wrong folder. | Run `cd <repo path>` first, then use `--target .`. |
| `devspec init` reports conflicts. | Review the files. Use `--force` only for reviewed framework-owned files. |
