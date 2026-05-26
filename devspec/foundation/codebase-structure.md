# Codebase Structure

Use this artifact to help developers and agents decide where work belongs, which repositories are usable, and which boundaries must be preserved. Keep repository trees selective and keep optional tables only when they contain real project facts or unresolved blockers.

## Repository Layouts

Use this section for selective repository trees, up to a maximum of 4-5 levels, that help agents decide where to create, edit, or inspect files. Include important source roots, feature or module folders, tests, scripts, config, infrastructure, docs, and routing-critical files when relevant. Do not list every file. When deeper detail is needed for placement, capture the specific path or rule in `Work Areas and Boundaries` instead of expanding the tree. Omit paths excluded by `devspec/foundation/discovery-exclusions.md` unless a project override marks them source-owned.

Use one `### Repository: <repository-name>` subsection per repository when multiple repositories participate.

### Repository: <repository-name>

```text
<repository-name>/
|-- <source-root>/
|   |-- <feature-or-module>/
|   |   |-- <components-or-handlers>/
|   |   `-- <services-or-utils>/
|-- <tests>/
|   |-- <unit-or-integration>/
|   `-- <e2e>/
|-- <scripts-or-tools>/
|-- <config-or-infra>/
|-- <docs>/
`-- <routing-or-package-file>
```

## Repository Configuration

Use this section only when multiple repositories participate in delivery, or when a non-default repository path or access limit affects work. Do not omit it for multi-repo sources or dependencies; record missing role, workspace, path, or access facts as blockers instead of dropping the section.

Rows may be seeded from named `/devspec.extract` input such as `UI - D:\repo-ui, API - D:\repo-api`. Use the supplied label as the initial repository name and role candidate, then refine it with evidence or user confirmation.

| Repository | Role | Local path | In current workspace | Access requirement | Evidence | Confidence | Work guidance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <repository-name> | <delivery-role> | <local-path-or-unknown> | yes, no, unknown | See `devspec/glossary.md#access-requirement-values` | <input-or-source> | confirmed, observed, inferred, blocked | <how work should use-or-avoid-this-repository> |

Do not infer access from repository location. For missing or ambiguous access requirements, ask the user to confirm one value from `devspec/glossary.md#access-requirement-values` before relying on the row.

## Work Areas and Boundaries

Use this section for internal file-placement decisions: modules, bounded contexts, layers, shared packages, ownership or review routing, and cross-cutting code placement. Put a fact here only when it tells future work where code belongs, who owns it, what must not cross a boundary, or how related code should be grouped. Put external service, API, event, database, or cross-repo contracts in `Integration Contracts` instead.

Common area types include `module`, `feature`, `layer`, `service`, `shared-package`, `cross-cutting`, and `ownership`.

| Scope | Area | Area type | Responsibility | Key paths | Boundary or placement rule | Owner or reviewer | Evidence | Confidence | Work guidance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| repository:<repository-name> | <area-name> | <area-type> | <primary-responsibility> | <path-or-pattern> | <allowed-dependencies-placement-or-review-rule> | <owner-team-reviewer-or-unknown> | <source-path-or-input> | confirmed, observed, inferred, blocked | <what future work should do> |

## Integration Contracts

Use this section for boundaries between repositories, modules, services, users, data stores, queues, APIs, providers, or external systems. A row belongs here when future work must preserve a protocol, data shape, dependency direction, lifecycle, or validation expectation.

| Source scope | Target or system | Contract or interface | Direction | Data or protocol | Required handling | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| repository:<repository-name> | <target-system> | <api-event-db-package-or-user-contract> | inbound, outbound, bidirectional | <data-shape-or-protocol> | <what to preserve-or-validate> | <source-path-or-input> | confirmed, observed, inferred, blocked |

## Structure Gaps and Blockers

Use this section only for missing or conflicting facts that prevent reliable repository selection, file placement, access validation, ownership routing, or integration handling. Do not duplicate normal open risks from work-item artifacts.

| Gap or blocker | Affected section | Impact | Required resolution | Status |
| --- | --- | --- | --- | --- |
| <missing-or-conflicting-fact> | Repository Configuration, Work Areas and Boundaries, Integration Contracts, or Repository Layouts | <why agents cannot proceed safely> | <question-evidence-or-access-needed> | open |
