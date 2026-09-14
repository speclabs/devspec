# Release packaging

This guide is for maintainers who build and publish the `devspec` CLI. Users install it through the [setup routes](../README.md#choose-a-setup-route).

## Version source

The package version has one source: `__version__` in `src/devspec/__init__.py`. `pyproject.toml` reads it dynamically. Every tag-triggered workflow runs `scripts/verify_release_version.py`, so a `vX.Y.Z` tag must equal that value before any artifact is built or published.

## Pipelines

| Workflow | Trigger | Builds | Publishes |
|---|---|---|---|
| `python-package-ci.yml` | Push to `main`, pull request, manual | Tests on Ubuntu, macOS, and Windows with Python 3.10 and 3.14; wheel and sdist; wheel smoke test | Nothing |
| `python-package-publish.yml` | `v*` tag, manual | Wheel, sdist, and `devspec-python-package-checksums.txt` | PyPI and the GitHub release on a tag; TestPyPI only when a manual run selects `testpypi` |
| `winget-package-publish.yml` | `v*` tag, manual | Portable `devspec.exe`, `devspec.exe.sha256`, and versioned WinGet manifests | The GitHub release on a tag |
| `homebrew-package-publish.yml` | `v*` tag, manual | Tap-ready `Formula/devspec.rb` and the source-tarball SHA-256 | Nothing |

No workflow writes to `microsoft/winget-pkgs` or the Homebrew tap. Those submissions are manual steps in the release checklist below.

Templates live in `packaging/`: `winget/SpecLabs.Devspec*.yaml` and `homebrew/devspec.rb`. The workflows replace their `REPLACE_WITH_*` placeholders and fail if any remain.

## One-time setup

- **PyPI.** The `devspec` project's trusted publisher must name repository `speclabs/devspec` and workflow `python-package-publish.yml`. Register the same publisher on TestPyPI before using the manual `testpypi` option.
- **Homebrew.** The tap is the `speclabs/homebrew-tap` repository; users install with `brew install speclabs/tap/devspec`.
- **WinGet.** The package identifier is `SpecLabs.Devspec`.

## Local verification

```bash
uv run python -m unittest discover -s tests
uv build
uvx --from dist/devspec-X.Y.Z-py3-none-any.whl devspec --version
```

`uv build` creates the sdist first and builds the wheel from it. That proves `MANIFEST.in` ships the `devspec/` artifacts, which `setup.py` bundles into the wheel under `devspec/_assets/`.

## Release checklist

1. Update `__version__` in `src/devspec/__init__.py`, merge to `main`, and confirm `Python Package CI` passes.
2. Optional rehearsal: run `WinGet Package Publish` manually on `main` to prove the executable builds, and run `Python Package Publish` with `testpypi` to rehearse the upload.
3. Tag the merged commit and push the tag:

   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

4. Confirm that the three tag workflows pass, PyPI lists the version, and the GitHub release carries the Python artifacts, `devspec.exe`, `devspec.exe.sha256`, and the WinGet manifests.
5. **WinGet.** Download the `devspec-winget-package` artifact and validate its `manifests/s/SpecLabs/Devspec/X.Y.Z/` folder:

   ```powershell
   winget validate --manifest <folder>
   winget install --manifest <folder>
   ```

   Installing from a local manifest requires `winget settings --enable LocalManifestFiles` from an administrator terminal. Then open a pull request that adds the folder to `microsoft/winget-pkgs`.
6. **Homebrew.** Download the `devspec-homebrew-package` artifact, copy its formula into the tap, and validate it:

   ```bash
   brew tap speclabs/tap
   cp Formula/devspec.rb "$(brew --repo speclabs/tap)/Formula/devspec.rb"
   brew audit --strict speclabs/tap/devspec
   brew install --build-from-source speclabs/tap/devspec
   brew test speclabs/tap/devspec
   ```

   Commit and push the formula from `$(brew --repo speclabs/tap)`. The formula pins `setuptools`, which Homebrew needs because it builds without isolation. When `pyproject.toml` raises the setuptools minimum, update that resource's URL and SHA-256 from the [setuptools files on PyPI](https://pypi.org/project/setuptools/#files).
7. Smoke-test each channel on a clean machine: `devspec --version`, then `devspec init` and `devspec doctor` against an empty directory.

## Rerun or recover

- The Python and WinGet workflows both attach files to the same GitHub release. If one fails while the other is creating the release, re-run the failed workflow.
- PyPI rejects a second upload of an existing version. If the upload succeeded and a later step failed, re-run only the failed steps, or fix forward with a new patch version.
- Run `Homebrew Package Publish` manually with a released version to regenerate its formula. The `vX.Y.Z` tag must exist and match the checked-out package version, so run it from the tag.
