# Implement

Use this artifact for recovery, audit, and handoff during implementation. Keep resume, task state, checkpoints, changed files, validation, blockers, and next handoff current. Omit optional sections with no entries.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | implement |
| Current command | `/devspec.implement` |
| Current agent | devspec.implement-task |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.implement` |
| Resume notes | |
| Updated | |

## Implementation Status

| Field | Value |
| --- | --- |
| Status | See `devspec/glossary.md#task-status-values` |
| Current task | |
| Completion note | |

## Progress Summary

| Completed | Pending | Skipped | Last confirmation outcome |
| --- | --- | --- | --- |
| <count> | <count> | <count> | proceed, continue, pause, skip, custom |

## Repo Access Validation

Include this section only when `Multi-repo dependency` is `yes` or implementation needs explicit repo access confirmation.

- Repo path source: `devspec/foundation/codebase-structure.md` when `Multi-repo dependency` is `yes`

| Repo | Access requirement | Access status | Notes |
| --- | --- | --- | --- |
| <repo-name> | <access-requirement> | <access-status> | |

## Task State

| Task | Target repo | Target area | Depends on | Status | Attempt count | Last checkpoint | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 |  |  |  | pending | 0 |  | |

## Last Safe Checkpoint

| Field | Value |
| --- | --- |
| Last completed task | |
| Current task | |
| Validation last run | |
| Known good state | |
| Roll-forward notes | |

## Changed Files

Include this section only after files or project artifacts change.

| File | Change summary | Status | Validation |
| --- | --- | --- | --- |
|  |  | modified |  |

## Task Execution Log

| Date | Task | Target repo | Target area | Attempt count | Status | Summary | Files changed | Validation | Blockers | Failed method | Failure reason | Retry condition | Next safer method | Confirmation after task |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | 0 | pending |  |  |  |  |  |  |  |  |  |

## Execution Summary

Include this section when pausing, completing, skipping, or handing off.

| Type | Item | Evidence or next action | Status |
| --- | --- | --- | --- |
| Current task outcome |  |  | pending |
| Completed task |  |  | complete |
| Overall completed summary |  |  | |
| Pending task |  |  | pending |
| Skipped task |  |  | skipped |
| Residual risk |  |  | open |
| Follow-up |  |  | open |

## Type-Specific Handling

Include this section only for bug or security-vulnerability work items, or when rules add type-specific handling.

| Type | Note |
| --- | --- |
| Rule source | `devspec/foundation/rules.md` |
| Bug handling notes | |
| Security handling notes | |

## Attempt Escalations

Include this section only when retry or repair attempts need escalation.

| Attempt | Reason | Escalation | Status |
| --- | --- | --- | --- |
| 1 |  |  | pending |

## Next Task Handoff

| Field | Value |
| --- | --- |
| Next task | |
| Preconditions | |
| Notes for next implementation pass | |
