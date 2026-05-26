# Tech Stack

Use this artifact for technology, version, support, hosting, and delivery facts that affect implementation or validation decisions.

## Stack Documentation Policy

| Policy area | Requirement |
| --- | --- |
| Evidence sources | Use manifests, lockfiles, framework config, CI config, infrastructure config, and docs as version evidence. |
| Discovery boundary | Do not inspect dependency folders, generated output, or excluded paths listed in `devspec/foundation/discovery-exclusions.md`. |
| Inventory scope | Use one stack inventory table per repo, deployable unit, or named project component. |
| Categories | Use clear categories such as `Language`, `Runtime`, `Framework`, `Library`, `Database`, `Service`, `Tooling`, `Hosting`, or `Delivery Constraint`. |
| Support status | Record support status from official release, lifecycle, or support pages when practical. |
| Unknown support | Use `no LTS channel`, `managed service`, or `unknown - needs lookup` instead of defaulting to `n/a`. |
| Not applicable support | Use `n/a` only when version support does not apply. |
| Verification date | Fill `Verified on` with the date the version or support status was checked. |
| Implementation impact | Include guidance when a technology affects coding, validation, hosting, compatibility, or support decisions. |
| Blocked facts | Record blocked stack, version, support, or hosting details as inventory rows with `blocked` confidence, the evidence gap, and the next action. |
| Row quality | Omit rows for technologies that are not confirmed, observed, inferred, or blocked by a specific evidence gap. |

## Stack Inventory

### Project: <project-name>

| Category | Technology | Project version or configuration | Support status | Evidence | Confidence | Verified on | Implementation impact or next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Runtime | <runtime> | <version> | <lts-version-or-status> | <manifest-or-doc-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |
| Framework | <framework> | <version> | <lts-version-or-status> | <manifest-or-config-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |
| Service | <service-or-platform> | <version-or-managed-plan> | <managed-service-or-support-status> | <config-or-doc-path> | observed | <yyyy-mm-dd> | <implementation-or-validation-impact> |
| Delivery Constraint | <blocked-or-unknown-stack-fact> | unknown | unknown - needs lookup | <missing-or-inconclusive-evidence> | blocked | <yyyy-mm-dd> | <next-action-needed> |

## Support Lifecycle References

Maintain this lookup with official release, lifecycle, or support pages. Update these sources when a project uses a different vendor distribution or a better official endpoint becomes available.

| Technology or ecosystem | Official source | Lookup guidance | Verified on |
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
