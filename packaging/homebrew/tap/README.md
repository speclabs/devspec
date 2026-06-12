# SpecLabs Homebrew Tap Package

This directory contains the tap-ready files for `speclabs/homebrew-tap`.

Initial deployment is source-only. Bottles should be added after the formula has passed source install validation on macOS and Linux.

## Publish

Create or update the public tap repository:

```text
brew tap-new speclabs/tap
```

Copy this directory into the tap repository so the formula lands at:

```text
Formula/devspec.rb
```

Commit and push the tap. Users can then install with:

```text
brew install speclabs/tap/devspec
```

## Validate

Run these checks from the tap repository:

```text
brew audit --new --formula Formula/devspec.rb
brew install --build-from-source Formula/devspec.rb
brew test devspec
devspec version
devspec init --target "$(mktemp -d)" --profile core --repo-state existing
```

After the public tap is pushed, verify a clean install:

```text
brew install speclabs/tap/devspec
devspec doctor --target . --profile core
```

## Update A Release

For each new `devspec` tag:

1. Update `url` to the new GitHub tag tarball.
2. Update `sha256` with the tag tarball checksum.
3. Run `brew update-python-resources --print-only devspec` from the tap when dependencies change.
4. Re-run the validation checks.
