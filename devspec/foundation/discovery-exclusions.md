# Discovery Exclusions

Use this file to keep discovery focused on project-owned source, configuration, tests, scripts, infrastructure, and docs.

Apply exclusions before broad search, extraction, code-pattern discovery, layout mapping, generated helper scripts, and validation discovery. Respect repository ignore files as a baseline while still applying this file. Do not infer coding standards, architecture, ownership, or implementation behavior from installed dependencies, generated output, caches, coverage output, VCS internals, or tool output. Use manifests, lockfiles, framework config, CI config, docs, source roots, tests, and scripts as evidence instead. Omit excluded folders from layout maps unless `Project Overrides` includes them.

Record intentional exceptions in `Project Overrides` before relying on normally excluded paths or adding project-specific exclusions.

## Baseline Exclusions

Use these categories for every repository, regardless of ecosystem. Ecosystem rules below add framework-specific patterns and evidence hints; they do not replace these defaults.

| Category | Exclude by default | Reason | Include only if |
| --- | --- | --- | --- |
| VCS internals | `.git/`, `.svn/`, `.hg/` | Version-control metadata is not project source. | User explicitly asks for VCS internals. |
| Generated or build output | `dist/`, `build/`, `out/`, generated artifacts | Output can be stale, duplicated, minified, or machine-produced. | Output is intentionally source-owned and recorded in `Project Overrides`. |
| Test and coverage output | `coverage/`, `.nyc_output/`, test result folders | Reports are run artifacts, not source conventions. | User asks for coverage or test-output diagnostics. |
| Cache and temporary output | `.cache/`, `tmp/`, `temp/`, tool caches | Cache content is transient and often huge. | User asks for cache diagnostics. |
| Local IDE or machine metadata | `.idea/`, `.vscode/`, editor user settings | Local settings usually reflect one machine, not project standards. | Repository standards explicitly depend on these files. |
| Dependency installs and package caches | Installed dependency folders and package-manager caches | Third-party code and package caches should not drive project conventions. | Dependency source inspection is explicitly requested or overridden. |

## Ecosystem Discovery Rules

Use this table after detecting the ecosystem. Exclusions listed here are ecosystem-specific additions to `Baseline Exclusions`. Prefer evidence sources are safe discovery targets unless a project override says otherwise.

| Ecosystem or framework | Detect from | Additional exclusions | Prefer as evidence |
| --- | --- | --- | --- |
| JavaScript and TypeScript, Node.js | `package.json`, lockfiles, `.npmrc`, `.yarnrc*`, `pnpm-workspace.yaml` | `node_modules/`, `.npm/`, `.yarn/cache/`, `.pnpm-store/` | `package.json`, lockfiles, `tsconfig*.json`, scripts, source roots, tests |
| Angular | `angular.json`, `package.json`, `tsconfig*.json` | `.angular/`, `.nx/` | `angular.json`, `tsconfig*.json`, `src/`, `projects/`, tests |
| React, Vue, Vite, SvelteKit, Astro, Remix | `package.json`, `vite.config.*`, `vue.config.*`, `svelte.config.*`, `astro.config.*`, `remix.config.*` | `.vite/`, `.svelte-kit/`, `.astro/` | framework config, `src/`, `app/`, `pages/`, `components/`, tests |
| Next.js and Nuxt | `next.config.*`, `nuxt.config.*`, `package.json` | `.next/`, `.nuxt/`, `.output/`, `.vercel/` | framework config, `app/`, `pages/`, `components/`, `server/`, tests |
| Nx and Turborepo | `nx.json`, `workspace.json`, `project.json`, `turbo.json`, `pnpm-workspace.yaml` | `.nx/`, `.turbo/` | workspace config, project config, package scripts, source roots |
| .NET SDK, ASP.NET, Blazor, MAUI | `.sln`, `.csproj`, `.fsproj`, `Directory.Build.*`, `global.json` | `bin/`, `obj/`, `TestResults/`, `artifacts/`, `.vs/` | solution, project files, props, targets, app settings, source and tests |
| JVM: Java, Kotlin, Spring, Maven, Gradle | `pom.xml`, `build.gradle*`, `settings.gradle*`, `gradle.properties`, `src/main/` | `target/`, `.gradle/`, `.mvn/wrapper/maven-wrapper.jar` | build files, wrapper config, `src/`, resources, tests |
| Python, Django, Flask, FastAPI, pytest, Poetry, uv | `pyproject.toml`, `requirements*.txt`, `setup.py`, `tox.ini`, `poetry.lock`, `uv.lock`, `manage.py` | `.venv/`, `venv/`, `env/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.tox/`, `site-packages/`, `htmlcov/` | project metadata, lockfiles, app packages, source and tests |
| PHP, Composer, Laravel, Symfony | `composer.json`, `composer.lock`, `artisan`, `symfony.lock` | `vendor/`, `var/cache/`, `var/log/`, `storage/framework/`, `storage/logs/`, `bootstrap/cache/`, `public/build/` | composer files, framework config, `app/`, `src/`, routes, tests |
| Ruby, Bundler, Rails | `Gemfile`, `Gemfile.lock`, `.ruby-version`, `config/application.rb` | `vendor/bundle/`, `.bundle/`, `tmp/`, `log/`, `public/assets/`, `storage/` | Gemfile, lockfile, `app/`, `config/`, `lib/`, tests |
| Go | `go.mod`, `go.work` | module cache, generated `vendor/` unless source-owned, `bin/`, `coverage.out` | `go.mod`, `go.sum`, `go.work`, source and tests |
| Rust | `Cargo.toml`, `Cargo.lock` | `target/`, `tarpaulin-report.html` | manifests, lockfile, `src/`, tests, benches |
| Android | `settings.gradle*`, `build.gradle*`, `gradle.properties`, `AndroidManifest.xml` | `.gradle/`, `build/`, `app/build/`, `.cxx/`, `captures/` | Gradle files, manifests, `src/`, resources, tests |
| iOS, SwiftPM, CocoaPods | `Package.swift`, `*.xcodeproj`, `*.xcworkspace`, `Podfile`, `Cartfile` | `DerivedData/`, `Pods/`, `.build/`, `build/`, `xcuserdata/`, `Carthage/Build/` | package manifests, project/workspace files, `Sources/`, `Tests/`, app source |
| C/C++, CMake, Bazel, Meson, Make | `CMakeLists.txt`, `WORKSPACE`, `MODULE.bazel`, `BUILD.bazel`, `meson.build`, `Makefile` | `cmake-build-*/`, `bazel-*`, `CMakeFiles/`, generated `compile_commands.json` | build files, `src/`, `include/`, `tests/`, toolchain files |
| Data and ML: notebooks, MLflow, Weights & Biases, checkpoints | `*.ipynb`, `mlflow.yml`, `wandb/`, `requirements*.txt`, `pyproject.toml` | `.ipynb_checkpoints/`, `mlruns/`, `wandb/`, `checkpoints/`, `models/`, `outputs/`, `runs/`, `lightning_logs/` unless source-owned | notebooks, experiment config, requirements, source modules, tests, docs |
| Infrastructure as code: Terraform, Terragrunt, Pulumi, CDK, Serverless, Helm, Kustomize | `*.tf`, `.terraform.lock.hcl`, `terragrunt.hcl`, `Pulumi.yaml`, `cdk.json`, `serverless.yml`, `Chart.yaml`, `kustomization.yaml` | `.terraform/`, `.terragrunt-cache/`, `cdk.out/`, `.serverless/`, `.pulumi/`, `tfplan`, `crash.log`, packaged `*.tgz` charts | IaC source, lockfiles, modules, manifests, environment config, docs |

## Project Overrides

Use this table only when a project intentionally owns a normally excluded path or needs an additional exclusion. Overrides must be specific enough that future agents know whether to include the path for evidence, exclude it from broad discovery, or inspect it only for a named purpose.

| Scope | Pattern | Action | Purpose | Confirmed by |
| --- | --- | --- | --- | --- |
| <repo-or-area> | <path-or-glob> | include, exclude, include-for-purpose | <why-this-exception-exists> | <user-source-or-date> |
