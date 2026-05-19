# Discovery Exclusions

Use this file to keep repository discovery focused on project-owned source and configuration.

Agents must exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output paths by default. Use manifests, lockfiles, and framework config files to understand dependencies and tooling.

## Global Exclusions

| Pattern | Reason | Retry or include only if |
| --- | --- | --- |
| `.git/` | VCS internals, not project source | User explicitly asks for Git internals |
| `.svn/`, `.hg/` | VCS internals, not project source | User explicitly asks for VCS internals |
| `dist/`, `build/`, `out/` | Generated or build output | Output is intentionally source-owned and recorded below |
| `coverage/`, `.nyc_output/` | Test output | User asks for coverage artifacts |
| `.cache/`, `tmp/`, `temp/` | Cache or temporary output | User asks for cache diagnostics |
| `.idea/`, `.vscode/` | Local IDE metadata | Repository standards explicitly depend on these files |

## Ecosystem Exclusions

| Ecosystem or framework | Detect from | Exclude by default | Prefer as evidence |
| --- | --- | --- | --- |
| Node.js, Angular, React, Next, Vite | `package.json`, lockfiles, `angular.json`, `next.config.*`, `vite.config.*` | `node_modules/`, `.angular/`, `.next/`, `.turbo/`, `.vite/`, `dist/`, `build/`, `coverage/` | `package.json`, lockfiles, `angular.json`, `tsconfig*.json`, framework config |
| .NET | `.sln`, `.csproj`, `.fsproj`, `Directory.Build.*` | `bin/`, `obj/`, `TestResults/`, `artifacts/` | solution, project files, props, targets |
| Java, Maven, Gradle | `pom.xml`, `build.gradle*`, `settings.gradle*` | `target/`, `build/`, `.gradle/`, `out/` | build files, `src/`, wrapper config |
| Python | `pyproject.toml`, `requirements*.txt`, `setup.py`, `tox.ini` | `.venv/`, `venv/`, `env/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `site-packages/` | project metadata, requirements, source and tests |
| Rust | `Cargo.toml` | `target/` | manifests, `src/`, tests |
| Go | `go.mod`, `go.work` | module cache, generated `vendor/` unless source-owned | `go.mod`, `go.sum`, source and tests |

## Project Overrides

Use this table only when a project intentionally owns a normally excluded path or needs an additional exclusion.

| Scope | Pattern | Action | Reason | Confirmed by |
| --- | --- | --- | --- | --- |
|  |  | include/exclude |  |  |

## Notes

- Do not inspect dependency folders to infer coding standards, architecture, or ownership.
- Do inspect manifests and lockfiles as dependency and tooling evidence.
- Respect repository ignore files as a baseline, but keep these exclusions explicit because search tools may not honor every ignore rule.
- Keep repository layout maps selective and omit excluded folders unless an override includes them.
