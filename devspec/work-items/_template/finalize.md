# Implementation Readiness Brief

Use this artifact for readiness, foundation and architecture alignment, implementation scope, validation expectations, and handoff. Keep lifecycle recovery in `Resume State`, readiness gating in `Readiness Assessment`, task-planning facts in `Implementation Brief`, and proof expectations in `Validation Plan`. Omit unused placeholder rows and reference facts already owned by upstream artifacts.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | finalize |
| Current command | `/devspec.finalize` |
| Current agent | devspec.finalize |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | baseline or CR-### |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.finalize` |
| Resume notes | |
| Updated | |

## Readiness Assessment

| Field | Value |
| --- | --- |
| Type | feature, bug, security-vulnerability |
| Severity | bugs and security vulnerabilities only |
| Priority | features should record priority |
| Status | See `devspec/glossary.md#readiness-status-values`; use only `ready` or `not ready` for the overall decision |
| Blocking gates | gate IDs or none |
| Next action | `/devspec.tasks` when ready; `/devspec.clarify` or required `devspec/foundation/*` or `devspec/architecture/*` artifact update when not ready |
| Decision note | |
| Decision inputs | `story.md`, `clarify.md`, accepted `decisions.md` records, `devspec/constitution.md`, applicable foundation artifacts, `devspec/architecture/overview.md`, applicable `devspec/architecture/decisions/*.md`, `devspec/foundation/rules.md` |

Use readiness gates only for checks that decide whether task planning may proceed. Use readiness values from `devspec/glossary.md#readiness-status-values`; put implementation facts in `Implementation Brief`. Overall readiness is `ready` only when every applicable gate is `ready` or `not applicable`.

| ID | Check | Evidence source | Status | Blocking action |
| --- | --- | --- | --- | --- |
| RG-001 | Scope boundary | Implementation Brief | See `devspec/glossary.md#readiness-status-values` | |
| RG-002 | Acceptance criteria | Implementation Brief | See `devspec/glossary.md#readiness-status-values` | |
| RG-003 | Dependencies and repository readiness | Implementation Brief; `devspec/foundation/codebase-structure.md` | See `devspec/glossary.md#readiness-status-values` | |
| RG-004 | Type-specific facts | Implementation Brief; `devspec/foundation/rules.md` | See `devspec/glossary.md#readiness-status-values` | |
| RG-005 | Validation and delivery risk | Implementation Brief; Validation Plan | See `devspec/glossary.md#readiness-status-values` | |
| RG-006 | Foundation and architecture alignment | `devspec/constitution.md`; applicable foundation artifacts; `devspec/architecture/overview.md`; applicable ADRs | See `devspec/glossary.md#readiness-status-values` | |

## Implementation Brief

Use this as the single task-planning input table. Include only facts that affect scope, task decomposition, repository readiness, type-specific requirements, delivery risk, validation, or handoff. Keep local paths and access values in `devspec/foundation/codebase-structure.md`; put validation methods in `Validation Plan`. Use baseline IDs for original scope and `CR-###-*` IDs for accepted post-baseline change requests; append CR-scoped rows without rewriting prior baseline or CR rows.

| Type | ID | Item | Source | Task effect | Status |
| --- | --- | --- | --- | --- | --- |
| Scope: in | SCOPE-IN-001 or CR-001-SCOPE-IN-001 | <implementation-boundary> | <source-or-id> | plan within | confirmed |
| Scope: out | SCOPE-OUT-001 or CR-001-SCOPE-OUT-001 | <non-goal> | <source-or-id> | exclude | confirmed |
| Acceptance criterion | AC-001 or CR-001-AC-001 | <observable-outcome> | <source-or-id> | implement and validate | pending |
| Planning input | PI-001 or CR-001-PI-001 | <assumption-constraint-dependency-or-target-area> | <source-or-id> | <task impact> | pending |
| Foundation constraint | FC-001 | <principle-product-stack-or-operational-constraint> | <source-path-section-or-id> | <task-or-validation-impact> | pending |
| Architecture constraint | ARCH-001 | <architecture-boundary-contract-decision-or-gap> | <source-path-section-or-adr-id> | <task-or-validation-impact> | pending |
| Standards constraint | STD-001 | <coding-testing-review-or-anti-pattern-guidance> | <source-path-section-or-id> | <task-or-review-impact> | pending |
| Delivery gate | DG-001 | <gate-or-compliance-requirement> | <source-path-section-or-id> | <readiness-or-validation-impact> | pending |
| Validation requirement | VR-001 or CR-001-VR-001 | <proof-needed-for-criterion-risk-or-gate> | <source-or-id> | validate before completion | pending |
| Repository readiness | MR-001 | <repo-readiness-summary-or-n/a> | `devspec/foundation/codebase-structure.md` | blocks if missing | pending |
| Type-specific requirement | TS-001 | <bug-security-or-rule-fact> | <source-or-id> | plan, validate, or release | pending |
| Risk or follow-up | RISK-001 or CR-001-RISK-001 | <risk-or-handoff-item> | <source-or-id> | <delivery effect> | open |

## Validation Plan

Record validation for acceptance criteria, type-specific requirements, and material risks. Omit unused rows. Use `CR-###-VP-###` IDs for change-request validation rows.

| ID | Covers | Method or evidence | Expected signal | Status |
| --- | --- | --- | --- | --- |
| VP-001 or CR-001-VP-001 | AC-001 or CR-001-AC-001 | <test-command-review-or-manual-check> | <passing-signal> | pending |
