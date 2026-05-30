#!/usr/bin/env bash
set -euo pipefail

profile="${1:-all}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export UV_CACHE_DIR="${UV_CACHE_DIR:-$root/.uv-cache}"
temp_root="$(mktemp -d "${TMPDIR:-/tmp}/devspec-local-install.XXXXXX")"

cleanup() {
  rm -rf "$temp_root"
}
trap cleanup EXIT

cd "$root"
uv run devspec version
uv run devspec init --target "$temp_root" --profile "$profile" --repo-state existing
uv run devspec doctor --target "$temp_root" --profile "$profile"
uv run devspec diff --target "$temp_root" --profile "$profile"
uv run devspec sync --target "$temp_root" --profile "$profile" --dry-run

printf 'devspec local install smoke test passed: %s\n' "$temp_root"
