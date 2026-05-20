# Tech Stack

Use manifests, lockfiles, framework config, CI config, and docs as version evidence. Do not inspect installed dependency folders or generated output excluded by `devspec/foundation/discovery-exclusions.md`.

For `Current LTS Version`, record an official LTS version when one exists. Otherwise record the support status: `no LTS channel` when the technology has releases but no official LTS designation, `managed service` for hosted services without a user-selected version, or `unknown - needs lookup` when verification was not possible.

Use `n/a` only when version support does not apply. Fill `Verified As Of` with the date the value or status was checked.

## Projects

### Project: <project-name>

#### Languages And Runtimes

| Technology | Version In Project | Current LTS Version | Verified As Of | Notes |
| --- | --- | --- | --- | --- |
| <language-or-runtime> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |

#### Frameworks And Libraries

| Technology | Version In Project | Current LTS Version | Verified As Of | Notes |
| --- | --- | --- | --- | --- |
| <framework-or-library> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |

#### Services And Infrastructure

| Technology | Version In Project | Current LTS Version | Verified As Of | Notes |
| --- | --- | --- | --- | --- |
| <service-or-platform> | <version-or-managed-plan> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |

#### Tooling

| Tooling Area | Technology | Version In Project | Current LTS Version | Verified As Of | Notes |
| --- | --- | --- | --- | --- | --- |
| Build | <tool> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |
| Test | <tool> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |
| Lint | <tool> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |
| CI/CD | <tool> | <version> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |

#### Hosting And Delivery Constraints

| Area | Current Choice | Current LTS Version | Verified As Of | Notes |
| --- | --- | --- | --- | --- |
| Hosting | <hosting-target> | <lts-version-or-status> | <yyyy-mm-dd> | <notes> |
| Delivery Constraint | <constraint> | n/a | <yyyy-mm-dd> | <notes> |

## LTS Lookup Sources

Maintain this lookup with official release, lifecycle, or support pages. Users may update these sources when a project uses a different vendor distribution or a better official endpoint becomes available.

| Technology Or Ecosystem | Official Source | Lookup Guidance | Verified As Of |
| --- | --- | --- | --- |
| Node.js | https://nodejs.org/en/about/releases/ | Use active or maintenance LTS release lines. | 2026-05-20 |
| Python | https://devguide.python.org/versions/ | Use supported Python versions; Python does not label releases as LTS. | 2026-05-20 |
| Java SE | https://www.oracle.com/java/technologies/java-se-support-roadmap.html | Use the vendor-supported LTS line relevant to the chosen JDK distribution. | 2026-05-20 |
| .NET | https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core | Use releases marked LTS by Microsoft. | 2026-05-20 |
| Go | https://go.dev/doc/devel/release | Use the supported release policy; Go does not label releases as LTS. | 2026-05-20 |
| PHP | https://www.php.net/supported-versions | Use actively supported or security-supported PHP branches. | 2026-05-20 |
| Ruby | https://www.ruby-lang.org/en/downloads/branches/ | Use branches under normal or security maintenance; Ruby does not label releases as LTS. | 2026-05-20 |
| Angular | https://angular.dev/reference/releases | Use versions marked active or LTS by Angular. | 2026-05-20 |
| React | https://react.dev/community/versioning-policy | Use React release policy and security maintenance notes; React does not label releases as LTS. | 2026-05-20 |
| Next.js | https://nextjs.org/support-policy | Use versions covered by the official support policy and LTS policy. | 2026-05-20 |
| Vite | https://vite.dev/releases | Use the official release policy; Vite does not label releases as LTS. | 2026-05-20 |
| Laravel | https://laravel.com/docs/releases | Use the official support policy table for bug-fix and security-fix windows. | 2026-05-20 |

## Blockers

- Blocker 1:
