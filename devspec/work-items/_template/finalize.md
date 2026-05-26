# Finalize

Use this artifact as the implementation-ready brief. Keep only details that affect scope, readiness, task planning, validation, risk, or handoff.

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

## Readiness Summary

| Status | Blocking gates | Next action | Notes |
| --- | --- | --- | --- |
| <ready-or-not-ready> | <gate-ids-or-none> | `/devspec.tasks` when ready; `/devspec.clarify` or a required foundation update when not ready | <decision-note> |

## Readiness Gates

| ID | Check | Source section | Required for ready | Status | If not ready |
| --- | --- | --- | --- | --- | --- |
| RG-001 | Scope boundary | Final Scope | In-scope and out-of-scope boundaries are explicit and do not expand the story. | <ready-not-ready-or-not-applicable> | <clarification-or-scope-decision> |
| RG-002 | Acceptance criteria | Acceptance Criteria | Criteria are observable or testable enough for task planning and validation. | <ready-not-ready-or-not-applicable> | <criterion-or-validation-clarification> |
| RG-003 | Dependencies and repo access | Planning Inputs; Multi-Repo Configuration | Dependencies, target repos, repo configuration, and required access are confirmed or not applicable. | <ready-not-ready-or-not-applicable> | <dependency-or-access-resolution> |
| RG-004 | Type-specific facts | Work-Item Classification; Delivery Notes; `devspec/foundation/rules.md` | Feature priority, bug facts, or security-vulnerability facts required by project rules are captured or explicitly blocked. | <ready-not-ready-or-not-applicable> | <type-specific-question-or-rule-resolution> |
| RG-005 | Validation and risk direction | Acceptance Criteria; Delivery Notes | Validation expectations and material delivery risks are known enough to plan tasks, or marked not applicable. | <ready-not-ready-or-not-applicable> | <validation-or-risk-resolution> |

## Final Scope

| Scope | Boundary | Source | Task-planning rule |
| --- | --- | --- | --- |
| In scope | <implementation-boundary> | <story-clarify-or-user-input> | Tasks may be created only for this work. |
| Out of scope | <explicit-non-goal> | <story-clarify-or-user-input> | Tasks must not be created for this work. |

## Acceptance Criteria

| ID | Criterion | Status |
| --- | --- | --- |
| AC-001 |  | pending |

## Planning Inputs

Include only assumptions, constraints, dependencies, or repo facts that affect task planning.

| Type | Input | Source | Planning effect |
| --- | --- | --- | --- |
| Assumption | <assumption> | <story-clarify-or-user-input> | <how tasks should account for it> |
| Constraint | <constraint> | <foundation-or-story-source> | <limit-on-task-planning> |
| Dependency | <dependency-or-none> | <story-clarify-or-user-input> | <sequencing-or-blocker-effect> |

## Multi-Repo Configuration

Use this section only when `Multi-repo dependency` is `yes`.

| Field | Value |
| --- | --- |
| Config source | `devspec/foundation/codebase-structure.md` |
| Configuration status | configured, missing |
| Access requirement status | confirmed, missing, blocked |
| Missing configuration blocker | |

## Delivery Notes

Include this section only when risks, mitigations, validation notes, backport scope, release notes, or advisories are relevant.

| Type | Note | Status | Owner or follow-up |
| --- | --- | --- | --- |
| Risk |  | open | |
| Mitigation |  | pending | |
| Validation |  | pending | |
| Backport or patch scope |  | pending | |
| Release note or advisory |  | pending | |
