# Work-Item Intake

Use this artifact for one work item or story at a time. Keep identity and routing in `meta.md`; keep decisions in `decisions.md`; keep implementation-ready scope in `finalize.md`.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | story |
| Current command | `/devspec.story` |
| Current agent | devspec.story |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.story` |
| Resume notes | |
| Updated | |

## Source Record

| Field | Value |
| --- | --- |
| External reference | |
| Resolved summary shown | |
| Confirmation basis | `devspec/foundation/provider-integrations.md` |
| User confirmation | confirmed, rejected, pending |
| Manual intake used | yes, no |
| Manual description | |
| Manual acceptance criteria | |

## Summary

Use one short statement of the requested story and intended outcome.

| Field | Value |
| --- | --- |
| Summary | |

## Description

Record background, user or customer problem, affected scope, impact, and type-specific context. Keep repository access in `devspec/foundation/codebase-structure.md` and rules in `devspec/foundation/rules.md`.

| Field | Value |
| --- | --- |
| Problem or opportunity | |
| User or customer impact | |
| Affected components | |
| Affected versions | |
| Type-specific context | |

## Acceptance Criteria

Record specific, testable conditions that must be true for completion.

| ID | Criterion | Source | Status |
| --- | --- | --- | --- |
| AC-001 |  | confirmed, provider, manual, user | pending |

## Functional Requirements

Record expected system behavior.

| ID | Requirement | Source | Status |
| --- | --- | --- | --- |
| FR-001 |  | confirmed, provider, manual, user, discovery | open |

## Nonfunctional Requirements

Record quality attributes such as security, performance, reliability, accessibility, compliance, or scalability.

| ID | Requirement | Source | Status |
| --- | --- | --- | --- |
| NFR-001 |  | foundation, intake, rule, user, discovery | open |

## Edge Cases

Record boundary conditions, failure paths, unusual states, and exception handling.

| ID | Case | Source | Status |
| --- | --- | --- | --- |
| EDGE-001 |  | confirmed, provider, manual, user, discovery | open |

## Planning Signals

Record assumptions, dependencies, risks, blockers, type-specific facts, terms, and scope exclusions that affect clarification, finalization, planning, or validation. Omit low-impact notes and unused placeholder rows.

| Type | ID | Item | Source | Status |
| --- | --- | --- | --- | --- |
| Assumption | ASM-001 |  | confirmed, inferred, user | open |
| Dependency | DEP-001 | <dependency-or-none> | intake, user, discovery | open |
| Multi-repo dependency | DEP-REPO-001 | yes, no; related repositories: <repository-names-only> | confirmed, user | open |
| Risk | RISK-001 |  | intake, user, discovery | open |
| Blocker | BLK-001 |  | intake, user, discovery | open |
