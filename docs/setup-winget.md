# WinGet setup

Use this route on Windows when the `SpecLabs.Devspec` package is available from your WinGet source. These guides describe devspec 0.3.0 and later; releases 0.2.x and earlier used a different CLI, so follow [Upgrade from devspec 0.2.x](setup-lifecycle.md#upgrade-from-devspec-02x) if `devspec --version` fails or reports 0.2.x. If the package is unavailable or blocked by policy, use the [Python route](setup-python.md) or [manual copy from `main`](manual-copy.md).

## Install

```powershell
winget install --id SpecLabs.Devspec --exact
devspec --version
```

WinGet installs a portable `devspec.exe` and adds it to `PATH` for new terminals. Close and reopen the terminal if `devspec` is not found.

Upgrade with `winget upgrade --id SpecLabs.Devspec --exact`, and uninstall with `winget uninstall --id SpecLabs.Devspec --exact`. Uninstalling the CLI never removes the files it copied into a repository.

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
