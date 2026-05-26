# Codebase Structure

Use this artifact to help developers and agents decide where work belongs. Keep repository trees selective and keep optional boundary tables only when they contain real project facts.

## Repository Layout

Use a selective 4-5 level tree that helps agents decide where to create or edit files. Include important source roots, feature/module folders, tests, scripts, config, infrastructure, docs, and routing-critical files when relevant. Do not list every file. Omit paths excluded by `devspec/foundation/discovery-exclusions.md` unless a project override marks them source-owned.

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

Use this section only when multiple repos participate in delivery. Do not omit it for multi-repo sources or dependencies; record missing role, workspace, path, or access facts as blockers instead of dropping the section.

Rows may be seeded from named `/devspec.extract` input such as `UI - D:\repo-ui, API - D:\repo-api`. Use the supplied label as the initial repo name and role candidate, then refine it with evidence or user confirmation.

| Repo | Role | Local path | In current workspace | Access requirement | Evidence | Confidence | Work guidance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <repo-name> | <role> | <local-path> | yes | <access-requirement> | <input-or-source> | confirmed | <how work should use this repo> |

Do not infer access from repo location. For missing or ambiguous access requirements, ask the user to confirm one value from `devspec/glossary.md#access-requirement-values` before relying on the row.

## Modules And Boundaries

| Scope | Module | Responsibility | Key paths | Boundary rules | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <module-name> | <primary responsibility> | <path-or-pattern> | <allowed dependencies or ownership boundary> | <source-path-or-input> | observed |

## Ownership Boundaries

Include this section only when ownership or review routing is known.

| Scope | Area | Owner or team | Responsibility | Review or escalation path | Source | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <area-name> | <owner-or-team> | <what they own> | <review-or-escalation-path> | <source-path-or-input> | confirmed |

## Integration Boundaries

Include this section only when integration contracts or external systems are known.

| Source scope | Target or system | Boundary or contract | Direction | Data or protocol | Evidence | Confidence | Required handling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <target-system> | <api-event-db-or-package-contract> | inbound | <data-shape-or-protocol> | <source-path-or-input> | observed | <what to preserve or validate> |

## Cross-Cutting Concerns

Include this section only when placement rules affect future work.

| Scope | Concern | Placement | Applies to | Evidence | Confidence | Placement rule |
| --- | --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <concern-name> | <path-or-layer> | <modules-or-services> | <source-path-or-input> | observed | <where to add or change related code> |

## Blockers

Include this section only when repository, ownership, access, or boundary facts are blocked.

| Blocker | Impact | Status |
| --- | --- | --- |
|  |  | open |
