# Setup With WinGet

Use this guide on Windows when your machine allows approved WinGet packages. WinGet is Windows' package installer for command-line and desktop tools.

The public WinGet package identifier is `SpecLabs.Devspec`. If the package is unavailable on your machine because of source, network, or policy restrictions, use `uvx devspec ...` or manual copy as the fallback.

## Before You Start

- Use Windows PowerShell or the VS Code terminal.
- WinGet must be available. Use Microsoft Learn if you need setup details: [Install or use WinGet](https://learn.microsoft.com/windows/package-manager/winget/).
- Confirm WinGet is available:

  ```text
  winget --version
  ```

- Open your target repository in a terminal.

## Open A Terminal

In VS Code, use **Terminal > New Terminal**. If you are using Windows directly, open PowerShell.

## Install devspec

Install the CLI:

```text
winget install --id SpecLabs.Devspec
```

Confirm the command is available:

```text
devspec version
```

Go to your target repository:

```text
cd D:\code\my-app
```

Install devspec files into your repository:

```text
devspec init --target . --profile all --repo-state existing
```

Use `--repo-state new` for a repo that has little or no code yet:

```text
devspec init --target . --profile all --repo-state new
```

If WinGet is blocked but `uvx` is allowed, use:

```text
uvx devspec init --target . --profile all --repo-state existing
```

## Validate The Install

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

Upgrade the CLI:

```text
winget upgrade --id SpecLabs.Devspec
```

Check the installed CLI version:

```text
devspec version
```

Preview framework file changes before writing anything:

```text
devspec diff --target .
devspec sync --target . --profile all --dry-run
```

Apply the framework file upgrade after review:

```text
devspec sync --target . --profile all
```

## Uninstall devspec

Uninstall the CLI:

```text
winget uninstall --id SpecLabs.Devspec
```

This removes the `devspec` command from your machine. It does not remove devspec files already copied into a repository.

If you need to remove devspec from a repository, review the files in Git first and remove only the framework files your team no longer wants.

## Common Examples

Install all adapters into an existing repo:

```text
devspec init --target . --profile all --repo-state existing
```

Install into a new repo:

```text
devspec init --target . --profile all --repo-state new
```

Install only Copilot support:

```text
devspec init --target . --profile copilot --repo-state existing
```

Install only Codex support:

```text
devspec init --target . --profile codex --repo-state existing
```

Install only Cursor support:

```text
devspec init --target . --profile cursor --repo-state existing
```

Use an explicit target path:

```text
devspec init --target D:\code\my-app --profile all --repo-state existing
```

Validate an installed repository:

```text
devspec doctor --target . --profile all
```

Check the CLI version:

```text
devspec version
```

List the installed WinGet package:

```text
winget list --id SpecLabs.Devspec
```

## Argument Reference

| Argument | Meaning | Beginner explanation |
| --- | --- | --- |
| `winget --version` | Print the WinGet version. | Confirms WinGet is available on the machine. |
| `winget install --id SpecLabs.Devspec` | Install the devspec CLI. | Installs the approved WinGet package. |
| `winget upgrade --id SpecLabs.Devspec` | Upgrade the devspec CLI. | Updates the command-line tool. Run a dry-run sync afterward before changing repository files. |
| `winget uninstall --id SpecLabs.Devspec` | Uninstall the devspec CLI. | Removes the command from the machine. It does not remove files already copied into repositories. |
| `version` | Print the devspec CLI version. | Use this to confirm the command runs. It does not change files. |
| `init` | Install devspec files. | Copies framework files into your repo. |
| `--target .` | Target repo folder. | `.` means the folder your terminal is currently in. |
| `--profile all` | Install or check profile. | `all` installs every supported adapter. Required for `init` and `sync`; optional for `diff` and `doctor`, where omission uses the installed manifest profile or falls back to `all`. |
| `--repo-state existing` | Repo type. | Required for `init`. Use `existing` for most projects and `new` for empty or early repos. |
| `doctor` | Validate install. | Checks that the expected files exist. |
| `diff` | Compare files. | Shows installed/package version context, then checksum-based missing, modified, stale, protected, or profile-mismatched files without writing changes. |
| `sync` | Update framework-owned files. | Applies framework updates using checksum comparisons while preserving project-owned artifacts. |
| `--dry-run` | Preview a sync. | Shows what `sync` would change without writing files. |
| `--force` | Overwrite reviewed conflicts. | Applies to `init` and `sync`; use only after reading conflict output. |

## Troubleshooting

| Problem | What to try |
| --- | --- |
| `winget` is not found. | Use Windows App Installer or ask your IT team whether WinGet is disabled. |
| `SpecLabs.Devspec` is not found. | Check approved WinGet sources and network access. Use [uv and uvx](uv.md) or [manual copy](manual-copy.md) if the package source is blocked. |
| `devspec` is not found after install. | Close and reopen PowerShell so PATH changes reload. |
| `winget list --id SpecLabs.Devspec` shows multiple installed versions. | Remove the older entry through WinGet or Windows Apps, then reopen PowerShell and confirm `devspec version` reports the expected version. |
| PowerShell blocks a command. | Ask your team about execution policy or approved package sources. |
| Corporate software policy blocks WinGet. | Use [uv and uvx](uv.md) if allowed, or [manual copy](manual-copy.md). |
