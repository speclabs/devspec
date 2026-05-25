# Discovery Exclusions

Use this file to keep discovery focused on project-owned source, configuration, tests, scripts, and docs.

Exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output paths by default. Record intentional exceptions in `Project Overrides` before relying on them.

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
| JavaScript and TypeScript, Node.js | `package.json`, lockfiles, `.npmrc`, `.yarnrc*`, `pnpm-workspace.yaml` | `node_modules/`, `.npm/`, `.yarn/cache/`, `.pnpm-store/`, `dist/`, `build/`, `coverage/`, `.nyc_output/` | `package.json`, lockfiles, `tsconfig*.json`, scripts, source roots, tests |
| Angular | `angular.json`, `package.json`, `tsconfig*.json` | `node_modules/`, `.angular/`, `dist/`, `coverage/`, `.nx/` | `angular.json`, `tsconfig*.json`, `src/`, `projects/`, tests |
| React, Vue, Vite, SvelteKit, Astro, Remix | `package.json`, `vite.config.*`, `vue.config.*`, `svelte.config.*`, `astro.config.*`, `remix.config.*` | `node_modules/`, `dist/`, `build/`, `.vite/`, `.svelte-kit/`, `.astro/`, `.cache/`, `coverage/` | framework config, `src/`, `app/`, `pages/`, `components/`, tests |
| Next.js and Nuxt | `next.config.*`, `nuxt.config.*`, `package.json` | `node_modules/`, `.next/`, `.nuxt/`, `.output/`, `.vercel/`, `out/`, `dist/`, `coverage/` | framework config, `app/`, `pages/`, `components/`, `server/`, tests |
| Nx and Turborepo | `nx.json`, `workspace.json`, `project.json`, `turbo.json`, `pnpm-workspace.yaml` | `.nx/`, `.turbo/`, `node_modules/`, `dist/`, `coverage/` | workspace config, project config, package scripts, source roots |
| .NET SDK, ASP.NET, Blazor, MAUI | `.sln`, `.csproj`, `.fsproj`, `Directory.Build.*`, `global.json` | `bin/`, `obj/`, `TestResults/`, `artifacts/`, `.vs/` | solution, project files, props, targets, app settings, source and tests |
| JVM: Java, Kotlin, Spring, Maven, Gradle | `pom.xml`, `build.gradle*`, `settings.gradle*`, `gradle.properties`, `src/main/` | `target/`, `build/`, `.gradle/`, `out/`, `.mvn/wrapper/maven-wrapper.jar` | build files, wrapper config, `src/`, resources, tests |
| Python, Django, Flask, FastAPI, pytest, Poetry, uv | `pyproject.toml`, `requirements*.txt`, `setup.py`, `tox.ini`, `poetry.lock`, `uv.lock`, `manage.py` | `.venv/`, `venv/`, `env/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.tox/`, `site-packages/`, `htmlcov/` | project metadata, lockfiles, app packages, source and tests |
| PHP, Composer, Laravel, Symfony | `composer.json`, `composer.lock`, `artisan`, `symfony.lock` | `vendor/`, `var/cache/`, `var/log/`, `storage/framework/`, `storage/logs/`, `bootstrap/cache/`, `public/build/`, `coverage/` | composer files, framework config, `app/`, `src/`, routes, tests |
| Ruby, Bundler, Rails | `Gemfile`, `Gemfile.lock`, `.ruby-version`, `config/application.rb` | `vendor/bundle/`, `.bundle/`, `tmp/`, `log/`, `coverage/`, `public/assets/`, `storage/` | Gemfile, lockfile, `app/`, `config/`, `lib/`, tests |
| Go | `go.mod`, `go.work` | module cache, generated `vendor/` unless source-owned, `bin/`, `coverage.out` | `go.mod`, `go.sum`, `go.work`, source and tests |
| Rust | `Cargo.toml`, `Cargo.lock` | `target/`, `coverage/`, `tarpaulin-report.html` | manifests, lockfile, `src/`, tests, benches |
| Android | `settings.gradle*`, `build.gradle*`, `gradle.properties`, `AndroidManifest.xml` | `.gradle/`, `build/`, `app/build/`, `.cxx/`, `captures/` | Gradle files, manifests, `src/`, resources, tests |
| iOS, SwiftPM, CocoaPods | `Package.swift`, `*.xcodeproj`, `*.xcworkspace`, `Podfile`, `Cartfile` | `DerivedData/`, `Pods/`, `.build/`, `build/`, `xcuserdata/`, `Carthage/Build/` | package manifests, project/workspace files, `Sources/`, `Tests/`, app source |
| C/C++, CMake, Bazel, Meson, Make | `CMakeLists.txt`, `WORKSPACE`, `MODULE.bazel`, `BUILD.bazel`, `meson.build`, `Makefile` | `build/`, `cmake-build-*/`, `bazel-*`, `.cache/`, `out/`, `CMakeFiles/`, `compile_commands.json` when generated | build files, `src/`, `include/`, `tests/`, toolchain files |
| Data and ML: notebooks, MLflow, Weights & Biases, checkpoints | `*.ipynb`, `mlflow.yml`, `wandb/`, `requirements*.txt`, `pyproject.toml` | `.ipynb_checkpoints/`, `mlruns/`, `wandb/`, `checkpoints/`, `models/`, `outputs/`, `runs/`, `lightning_logs/` unless source-owned | notebooks, experiment config, requirements, source modules, tests, docs |
| Infrastructure as code: Terraform, Terragrunt, Pulumi, CDK, Serverless, Helm, Kustomize | `*.tf`, `.terraform.lock.hcl`, `terragrunt.hcl`, `Pulumi.yaml`, `cdk.json`, `serverless.yml`, `Chart.yaml`, `kustomization.yaml` | `.terraform/`, `.terragrunt-cache/`, `cdk.out/`, `.serverless/`, `.pulumi/`, `tfplan`, `crash.log`, packaged `*.tgz` charts | IaC source, lockfiles, modules, manifests, environment config, docs |

## Project Overrides

Use this table only when a project intentionally owns a normally excluded path or needs an additional exclusion.

| Scope | Pattern | Action | Reason | Confirmed by |
| --- | --- | --- | --- | --- |
|  |  | include/exclude |  |  |

## Notes

| Rule | Note |
| --- | --- |
| Dependency and generated paths | Do not inspect them to infer coding standards, architecture, or ownership. |
| Manifests and lockfiles | Inspect them as dependency and tooling evidence. |
| Ignore files | Respect them as a baseline; keep these exclusions explicit for tools that do not honor every ignore rule. |
| Layout maps | Keep them selective and omit excluded folders unless an override includes them. |
