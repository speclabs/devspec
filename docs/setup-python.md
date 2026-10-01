# Python and uvx setup

Use this route on Windows, macOS, or Linux when Python 3.10 or newer is available. Choose `uvx` for one-off use, or `uv tool` or `pipx` for a persistent CLI installation.

These guides describe devspec 0.3.0 and later. Releases 0.2.x and earlier shipped a different CLI and framework layout. If `devspec --version` fails or reports 0.2.x, upgrade the CLI with the commands below and then follow [Upgrade from devspec 0.2.x](setup-lifecycle.md#upgrade-from-devspec-02x). If the newest published release is still 0.2.x, or PyPI is unreachable, use [manual copy from `main`](manual-copy.md), which never requires Python or a package manager.

## One-off use with uvx

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) using your platform's supported method, then run devspec without a permanent installation:

```text
uvx devspec --version
```

`uvx` reuses a cached version when one exists. Use `uvx devspec@latest <command>` when you need the newest release.

## Persistent installation with uv

```text
uv tool install devspec
devspec --version
```

Upgrade with `uv tool upgrade devspec`, and uninstall with `uv tool uninstall devspec`.

## Persistent installation with pipx

On Windows:

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
```

On macOS or Linux:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Then, in a new terminal on any platform:

```text
pipx install devspec
devspec --version
```

Restart the terminal if `devspec` is not found after `ensurepath`. Upgrade with `pipx upgrade devspec`, and uninstall with `pipx uninstall devspec`.

Uninstalling the CLI never removes the files it copied into a repository.

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
