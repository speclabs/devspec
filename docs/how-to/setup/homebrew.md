# Setup With Homebrew

Use this guide when your macOS or Linux team already uses Homebrew. Homebrew is a developer package manager: it installs command-line tools and can update them later.

The Homebrew package is distributed through the SpecLabs tap when a tap release is available. Initial releases use a source formula; bottled packages may be added after source installs are stable on macOS and Linux.

## Before You Start

- Homebrew must be installed. Use the official site: [Install Homebrew](https://brew.sh/).
- The SpecLabs Homebrew tap must be reachable from your machine.
- Open your target repository in a terminal.

## Open A Terminal

On macOS, open Terminal, iTerm, or the VS Code terminal.

## Go To Your Target Repository

```text
cd /Users/me/code/my-app
```

## Install Or Run devspec

Install the CLI:

```text
brew install speclabs/tap/devspec
```

If the SpecLabs tap or the current `devspec` formula is not available in your environment yet, use [uv and uvx](uv.md) as the fallback.

Install devspec files into your repository:

```text
devspec init --target . --profile all --repo-state existing
```

Use `--repo-state new` for a repo that has little or no code yet:

```text
devspec init --target . --profile all --repo-state new
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

## Common Examples

Check the CLI version:

```text
devspec version
```

Install all adapters:

```text
devspec init --target . --profile all --repo-state existing
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

Update the CLI with Homebrew:

```text
brew upgrade devspec
```

Preview a framework file upgrade:

```text
devspec diff --target .
devspec sync --target . --profile all --dry-run
```

Apply the framework file upgrade after review:

```text
devspec sync --target . --profile all
```

Use an explicit target path:

```text
devspec init --target /Users/me/code/my-app --profile all --repo-state existing
```

## Argument Reference

| Argument | Meaning | Beginner explanation |
| --- | --- | --- |
| `brew install speclabs/tap/devspec` | Install the devspec CLI. | Installs from the public SpecLabs tap when the formula is published. Initial releases build from source. |
| `brew upgrade devspec` | Update the devspec CLI. | Updates the command-line tool. Run `devspec sync --target . --profile all --dry-run` afterward to preview framework file changes. |
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
| `brew` is not found. | Install Homebrew, or use [uv and uvx](uv.md). |
| `brew install speclabs/tap/devspec` fails. | Confirm the tap is published, reachable, and Homebrew can access GitHub. Use `uvx devspec ...` as the fallback. |
| `devspec` is not found after install. | Run `brew doctor`, then close and reopen your terminal. |
| Your team does not use Homebrew. | Use [uv and uvx](uv.md) instead. |
