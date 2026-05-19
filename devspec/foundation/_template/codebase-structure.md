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

| Repo | Role | Local path | In current workspace | Access requirement | Notes |
| --- | --- | --- | --- | --- | --- |
| <repo-name> | <role> | <local-path> | yes | <access-requirement> | |

Do not assume access requirements. A repo outside the current repo folder is not automatically `reference-only`; repo location, workspace membership, and access requirement are separate facts. For each repo with a missing or ambiguous access requirement, ask the user to confirm one access requirement with multiple-choice options before writing or relying on the row.

Access requirement values:

- `reference-only`: inspect for context only; do not edit or run project validation.
- `edit`: code or documentation changes are expected.
- `edit-and-test`: code or documentation changes and validation are expected.
- `validation-only`: run validation only; do not edit.
- `release-coordination`: track delivery dependency; edits require separate user confirmation.
- `blocked`: required repo is unavailable or inaccessible.

## Modules And Boundaries

| Scope | Module | Responsibility | Key paths | Boundary rules | Notes |
| --- | --- | --- | --- | --- | --- |
| repo:<repo-name> | <module-name> | <primary responsibility> | <path-or-pattern> | <allowed dependencies or ownership boundary> | |

## Ownership Seams

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

- Blocker 1:
