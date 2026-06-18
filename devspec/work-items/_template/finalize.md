# Implementation Readiness Brief

Use this artifact for readiness, implementation scope, validation expectations, and handoff. Omit unused placeholder rows and reference facts already owned by upstream artifacts.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | finalize |
| Current command | `/devspec.finalize` |
| Current agent | devspec.finalize |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
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
| Next action | `/devspec.tasks` when ready; `/devspec.clarify` or required foundation update when not ready |
| Decision note | |
| Decision inputs | `story.md`, `clarify.md`, accepted `decisions.md` records, `devspec/foundation/rules.md` |

Use readiness gates only for checks that decide whether task planning may proceed. Use readiness values from `devspec/glossary.md#readiness-status-values`; put implementation facts in `Implementation Brief`.

| ID | Check | Evidence source | Status | Blocking action |
| --- | --- | --- | --- | --- |
| RG-001 | Scope boundary | Implementation Brief | See `devspec/glossary.md#readiness-status-values` | |
| RG-002 | Acceptance criteria | Implementation Brief | See `devspec/glossary.md#readiness-status-values` | |
| RG-003 | Dependencies and repository readiness | Implementation Brief; `devspec/foundation/codebase-structure.md` | See `devspec/glossary.md#readiness-status-values` | |
| RG-004 | Type-specific facts | Implementation Brief; `devspec/foundation/rules.md` | See `devspec/glossary.md#readiness-status-values` | |
| RG-005 | Validation and delivery risk | Implementation Brief; Validation Plan | See `devspec/glossary.md#readiness-status-values` | |

## Implementation Brief

Use this as the single task-planning input table. Keep local paths and access values in `devspec/foundation/codebase-structure.md`; put validation methods in `Validation Plan`.

| Type | ID | Item | Source | Task effect | Status |
| --- | --- | --- | --- | --- | --- |
| Scope: in | SCOPE-IN-001 | <implementation-boundary> | <source-or-id> | plan within | confirmed |
| Scope: out | SCOPE-OUT-001 | <non-goal> | <source-or-id> | exclude | confirmed |
| Acceptance criterion | AC-001 | <observable-outcome> | <source-or-id> | implement and validate | pending |
| Planning input | PI-001 | <assumption-constraint-dependency-or-target-area> | <source-or-id> | <task impact> | pending |
| Repository readiness | MR-001 | <repo-readiness-summary-or-n/a> | `devspec/foundation/codebase-structure.md` | blocks if missing | pending |
| Type-specific requirement | TS-001 | <bug-security-or-rule-fact> | <source-or-id> | plan, validate, or release | pending |
| Risk or follow-up | RISK-001 | <risk-or-handoff-item> | <source-or-id> | <delivery effect> | open |

## Validation Plan

Record validation for acceptance criteria, type-specific requirements, and material risks. Omit unused rows.

| ID | Covers | Method or evidence | Expected signal | Status |
| --- | --- | --- | --- | --- |
| VP-001 | AC-001 | <test-command-review-or-manual-check> | <passing-signal> | pending |
