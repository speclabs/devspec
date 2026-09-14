# Homebrew setup

Use this route on macOS or Linux when the `devspec` formula is published to the SpecLabs tap, `speclabs/homebrew-tap`. These guides describe devspec 0.3.0 and later; releases 0.2.x and earlier used a different CLI, so follow [Upgrade from devspec 0.2.x](setup-lifecycle.md#upgrade-from-devspec-02x) if `devspec --version` fails or reports 0.2.x. If the tap or formula is unavailable, use the [Python route](setup-python.md) or [manual copy from `main`](manual-copy.md).

## Install

```bash
brew install speclabs/tap/devspec
devspec --version
```

The formula installs from the tagged GitHub source release, so the install needs network access to GitHub and PyPI.

Upgrade with `brew update && brew upgrade devspec`, and uninstall with `brew uninstall devspec`. Uninstalling the CLI never removes the files it copied into a repository.

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
