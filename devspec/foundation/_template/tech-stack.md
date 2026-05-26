# Tech Stack

## Recording Rules

- Use manifests, lockfiles, framework config, CI config, and docs as version evidence.
- Do not inspect dependency folders, generated output, or excluded paths listed in `devspec/foundation/discovery-exclusions.md`.
- Use one project table per repo or deployable unit.
- Use clear categories such as `Language`, `Runtime`, `Framework`, `Library`, `Database`, `Service`, `Tooling`, `Hosting`, or `Delivery Constraint`.
- Record `Current LTS/Support` from official release, lifecycle, or support pages when practical to verify.
- Use `no LTS channel`, `managed service`, or `unknown - needs lookup` instead of defaulting to `n/a`.
- Use `n/a` only when version support does not apply.
- Fill `Verified As Of` with the date the version or support status was checked.
- Include implementation guidance when the technology affects coding, validation, hosting, compatibility, or support decisions.
- Omit rows for technologies that are not confirmed, observed, inferred, or blocked by a specific evidence gap.

## Projects

### Project: <project-name>

| Category | Technology | Version In Project | Current LTS/Support | Evidence | Confidence | Verified As Of | Implementation guidance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Runtime | <runtime> | <version> | <lts-version-or-status> | <manifest-or-doc-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |
| Framework | <framework> | <version> | <lts-version-or-status> | <manifest-or-config-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |
| Service | <service-or-platform> | <version-or-managed-plan> | <lts-version-or-status> | <config-or-doc-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |

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

Include this section only when stack, version, support, or hosting details are blocked.

| Blocker | Impact | Status |
| --- | --- | --- |
|  |  | open |
