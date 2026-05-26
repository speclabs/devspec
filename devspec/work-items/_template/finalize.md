# Finalize

Use this artifact as the implementation-ready brief. Keep only details that affect readiness, final scope, acceptance criteria, task planning, validation, delivery risk, or handoff.

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

## Work-Item Classification

| Field | Value |
| --- | --- |
| Type | feature, bug, security-vulnerability |
| Severity | bugs and security vulnerabilities only |
| Priority | features should record priority |

## Readiness Decision

| Status | Blocking gates | Next action | Decision note |
| --- | --- | --- | --- |
| <ready-or-not-ready> | <gate-ids-or-none> | `/devspec.tasks` when ready; `/devspec.clarify` or a required foundation update when not ready | <decision-note> |

## Readiness Gates

| ID | Check | Evidence source | Ready condition | Status | Blocking action |
| --- | --- | --- | --- | --- | --- |
| RG-001 | Scope boundary | Final Scope | In-scope and out-of-scope boundaries are explicit and do not expand the story. | <ready-not-ready-or-not-applicable> | <clarification-or-scope-decision> |
| RG-002 | Acceptance criteria | Acceptance Criteria | Criteria are observable or testable enough for task planning and validation. | <ready-not-ready-or-not-applicable> | <criterion-or-validation-clarification> |
| RG-003 | Dependencies and repo readiness | Task Planning Inputs; Multi-Repo Readiness | Dependencies are captured and required repo configuration or access is confirmed or not applicable. Missing or blocked repo readiness keeps the gate not ready. | <ready-not-ready-or-not-applicable> | <dependency-or-access-resolution> |
| RG-004 | Type-specific facts | Work-Item Classification; Type-Specific Requirements; `devspec/foundation/rules.md` | Feature priority, bug facts, or security-vulnerability facts required by project rules are captured or explicitly blocked. | <ready-not-ready-or-not-applicable> | <type-specific-question-or-rule-resolution> |
| RG-005 | Validation and delivery risk | Validation Plan; Risks And Follow-Up | Validation expectations and material delivery risks are known enough to plan tasks, or marked not applicable. | <ready-not-ready-or-not-applicable> | <validation-or-risk-resolution> |

## Final Scope

| Scope | Boundary | Source | Task-planning rule |
| --- | --- | --- | --- |
| In scope | <implementation-boundary> | <story-clarify-or-user-input> | Tasks may be created only for this work. |
| Out of scope | <explicit-non-goal> | <story-clarify-or-user-input> | Tasks must not be created for this work. |

## Acceptance Criteria

Record what must be true after implementation. Put validation method details in `Validation Plan`.

| ID | Criterion | Status |
| --- | --- | --- |
| AC-001 |  | pending |

## Task Planning Inputs

Include only assumptions, constraints, dependencies, or target-area facts that affect task decomposition. Do not duplicate scope boundaries, acceptance criteria, validation methods, or multi-repo configuration.

| Type | Input | Source | Planning effect |
| --- | --- | --- | --- |
| Assumption | <assumption> | <story-clarify-or-user-input> | <how tasks should account for it> |
| Constraint | <constraint> | <foundation-or-story-source> | <limit-on-task-planning> |
| Dependency | <dependency-or-none> | <story-clarify-or-user-input> | <sequencing-or-blocker-effect> |
| Target area | <repo-module-area-or-surface> | <foundation-story-or-discovery-source> | <where tasks should focus> |

## Multi-Repo Readiness

Use this section only when `Multi-repo dependency` is `yes`.

| Field | Value |
| --- | --- |
| Config source | `devspec/foundation/codebase-structure.md` |
| Configuration status | configured, missing, blocked |
| Required repos | |
| Access confirmation status | confirmed, missing, blocked |
| Blocking gap | |

## Type-Specific Requirements

Include this section only for bug or security-vulnerability work items, or when `devspec/foundation/rules.md` adds type-specific readiness facts.

| Type | Requirement | Source | Status |
| --- | --- | --- | --- |
| Bug | <expected-actual-repro-impact-regression-context> | <story-clarify-or-rule-source> | pending |
| Security | <severity-scope-attack-surface-exploitability-disclosure-containment> | <story-clarify-or-rule-source> | pending |

## Validation Plan

Record how acceptance criteria, type-specific requirements, and material risks should be validated.

| ID | Covers | Method or evidence | Expected signal | Status |
| --- | --- | --- | --- | --- |
| VP-001 | AC-001 | <test-command-review-or-manual-check> | <passing-signal> | pending |

## Risks And Follow-Up

Include this section only when risks, mitigations, backport scope, release notes, advisories, or handoff follow-ups affect delivery.

| Type | Note | Status | Owner or follow-up |
| --- | --- | --- | --- |
| Risk |  | open | |
| Mitigation |  | pending | |
| Backport or patch scope |  | pending | |
| Release note or advisory |  | pending | |
| Follow-up |  | open | |
