# Finalize

Use this artifact as the implementation-ready brief. Keep only details that affect readiness, implementation scope, task planning, validation, delivery risk, or handoff. Put lifecycle recovery in `Resume State`, readiness gating in `Readiness`, implementation facts in `Implementation Brief`, and proof expectations in `Validation Plan`.

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

## Readiness

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

Use readiness gates only for checks that decide whether task planning may proceed. Record the missing fact or blocking action here; record implementation content in `Implementation Brief`.

| ID | Check | Evidence source | Ready condition | Status | Blocking action |
| --- | --- | --- | --- | --- | --- |
| RG-001 | Scope boundary | Implementation Brief | In-scope and out-of-scope boundaries are explicit and do not expand the story. | See `devspec/glossary.md#readiness-status-values` | |
| RG-002 | Acceptance criteria | Implementation Brief | Criteria are observable or testable enough for task planning and validation. | See `devspec/glossary.md#readiness-status-values` | |
| RG-003 | Dependencies and repo readiness | Implementation Brief; `devspec/foundation/codebase-structure.md` | Dependencies are captured and required repo configuration or access is confirmed or not applicable. | See `devspec/glossary.md#readiness-status-values` | |
| RG-004 | Type-specific facts | Implementation Brief; `devspec/foundation/rules.md` | Feature priority, bug facts, or security-vulnerability facts required by project rules are captured or explicitly blocked. | See `devspec/glossary.md#readiness-status-values` | |
| RG-005 | Validation and delivery risk | Implementation Brief; Validation Plan | Validation expectations and material delivery risks are known enough to plan tasks, or marked not applicable. | See `devspec/glossary.md#readiness-status-values` | |

## Implementation Brief

Use this as the single task-planning input table. Include only facts that affect scope, acceptance criteria, task decomposition, repo readiness, type-specific requirements, delivery risk, or handoff. For multi-repo work, summarize readiness here and keep local paths and access requirement values in `devspec/foundation/codebase-structure.md`. Put validation methods in `Validation Plan`.

| Type | ID | Item | Source | Task-planning or delivery effect | Status |
| --- | --- | --- | --- | --- | --- |
| Scope: in | SCOPE-IN-001 | <implementation-boundary> | <story-clarify-decision-or-user-input> | Tasks may be created only for this work. | confirmed |
| Scope: out | SCOPE-OUT-001 | <explicit-non-goal> | <story-clarify-decision-or-user-input> | Tasks must not be created for this work. | confirmed |
| Acceptance criterion | AC-001 | <observable-outcome> | <story-clarify-decision-or-user-input> | Drives implementation tasks and validation coverage. | pending |
| Planning input | PI-001 | <assumption-constraint-dependency-or-target-area> | <foundation-story-clarify-decision-or-discovery-source> | <how tasks should account for it> | pending |
| Repo readiness | MR-001 | <required-repos-and-access-confirmation-summary-or-not-applicable> | `devspec/foundation/codebase-structure.md` | Missing or blocked repo readiness prevents task planning. | pending |
| Type-specific requirement | TS-001 | <bug-security-or-rule-required-fact> | <story-clarify-decision-or-rule-source> | Required for task planning, validation, or release handling. | pending |
| Risk or follow-up | RISK-001 | <risk-mitigation-backport-release-note-advisory-or-handoff-item> | <story-clarify-decision-or-discovery-source> | <delivery-or-handoff-effect> | open |

## Validation Plan

Record how acceptance criteria, type-specific requirements, and material risks should be validated.

| ID | Covers | Method or evidence | Expected signal | Status |
| --- | --- | --- | --- | --- |
| VP-001 | AC-001 | <test-command-review-or-manual-check> | <passing-signal> | pending |
