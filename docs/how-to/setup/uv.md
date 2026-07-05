# Setup With uv and uvx

Use this guide when you want the simplest command-line setup. `uvx devspec ...` downloads and runs `devspec` for one command without permanently installing the `devspec` command.

## Before You Start

- You need `uv` installed. Use the official guide: [Install uv](https://docs.astral.sh/uv/getting-started/installation/).
- `uvx devspec ...` runs `devspec` for one command without permanently installing the `devspec` command.
- `uv tool install devspec` installs the `devspec` command in your user-local tool directory.
- Run `devspec init`, `devspec doctor`, and `devspec sync` from the repository you want to update.

## Open A Terminal

In VS Code, use **Terminal > New Terminal**.

## Set Up devspec

Go to your target repository.

Windows PowerShell:

```text
cd D:\code\my-app
```

macOS/Linux:

```text
cd /Users/me/code/my-app
```

Choose one setup path.

Recommended one-time setup with `uvx`:

```text
uvx devspec init --target . --profile all --repo-state existing
```

Use `--repo-state new` for a repo that has little or no code yet:

```text
uvx devspec init --target . --profile all --repo-state new
```

If you want a reusable local `devspec` command instead of `uvx`, use the persistent local install:

```text
uv tool install devspec
devspec version
devspec init --target . --profile all --repo-state existing
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

## Upgrade devspec

If you use `uvx`, there is no persistent `devspec` command to upgrade. Run upgrade checks from the repository that already has devspec installed:

```text
uvx devspec diff --target .
uvx devspec sync --target . --profile all --dry-run
```

If you installed the persistent command, upgrade the CLI:

```text
uv tool upgrade devspec
```

Check the installed CLI version:

```text
devspec version
```

From the repository that already has devspec installed, preview framework file changes before writing anything:

```text
devspec diff --target .
devspec sync --target . --profile all --dry-run
```

Apply the framework file upgrade after review:

```text
devspec sync --target . --profile all
```

## Uninstall devspec

If you installed the persistent command, uninstall the CLI:

```text
uv tool uninstall devspec
```

There is no persistent `devspec` command to uninstall when you only use `uvx`.

The uninstall command removes the `devspec` command from your machine. It does not remove devspec files already copied into a repository.

If you need to remove devspec files from a repository, review the files in Git first and remove only the framework files your team no longer wants.

## Common Examples

Check the CLI version:

```text
uvx devspec version
```

Install all adapters into an existing repo:

```text
uvx devspec init --target . --profile all --repo-state existing
```

Install into a new repo:

```text
uvx devspec init --target . --profile all --repo-state new
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

Apply framework file changes after review:

```text
uvx devspec sync --target . --profile all
```

Use an explicit target path:

```text
uvx devspec init --target D:\code\my-app --profile all --repo-state existing
uvx devspec init --target /Users/me/code/my-app --profile all --repo-state existing
```

List persistent uv tools:

```text
uv tool list
```

## Argument Reference

| Argument | Meaning | Beginner explanation |
| --- | --- | --- |
| `uvx devspec` | Run devspec once through uv. | Downloads and runs the CLI for this command. |
| `uv tool install devspec` | Install devspec as a user-local tool. | Makes the `devspec` command available for later terminal sessions when PATH is configured. |
| `uv tool upgrade devspec` | Upgrade the persistent devspec CLI. | Updates the user-local command. Run a dry-run sync from each repository before changing framework files. |
| `uv tool uninstall devspec` | Uninstall the persistent devspec CLI. | Removes the command from the machine. It does not remove files already copied into repositories. |
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
