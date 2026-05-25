# Codebase Structure

## Repository Layout

Use a selective 3-5 level tree that helps agents decide where to create or edit files. Include important source roots, feature/module folders, tests, scripts, config, infrastructure, docs, and routing-critical files when relevant. Do not list every file. Omit paths excluded by `devspec/foundation/discovery-exclusions.md` unless a project override marks them source-owned.

### Repo: <repo-name>

```text
<repo-name>/
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

## Repo Configuration

Use this section only when multiple repos participate in delivery.

Rows may be seeded from named `/devspec.extract` input such as `UI - D:\repo-ui, API - D:\repo-api`. Use the supplied label as the initial repo name and role candidate, then refine it with evidence or user confirmation.

| Repo | Role | Local path | In current workspace | Access requirement | Notes |
| --- | --- | --- | --- | --- | --- |
| <repo-name> | <role> | <local-path> | yes | <access-requirement> | |

Do not infer access from repo location. For missing or ambiguous access requirements, ask the user to confirm one value from `devspec/glossary.md#access-requirement-values` before relying on the row.

## Modules And Boundaries

| Scope | Module | Responsibility | Key paths | Boundary rules | Notes |
| --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <module-name> | <primary responsibility> | <path-or-pattern> | <allowed dependencies or ownership boundary> | |

## Ownership Boundaries

| Scope | Area | Owner or team | Responsibility | Review or escalation path | Notes |
| --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <area-name> | <owner-or-team> | <what they own> | <review-or-escalation-path> | |

## Integration Boundaries

| Source scope | Target or system | Boundary or contract | Direction | Data or protocol | Notes |
| --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <target-system> | <api-event-db-or-package-contract> | inbound | <data-shape-or-protocol> | |

## Cross-Cutting Concerns

| Scope | Concern | Placement | Applies to | Notes |
| --- | --- | --- | --- | --- |
| repo:<repo-name> | <concern-name> | <path-or-layer> | <modules-or-services> | |

## Blockers

| Blocker | Impact | Status |
| --- | --- | --- |
|  |  | open |
