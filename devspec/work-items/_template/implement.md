# Implementation Record

Use this artifact for recovery, audit, and handoff during implementation. Keep lifecycle recovery in `Resume State`, per-task progress in `Implementation Task Ledger`, changed files and validation evidence in `Implementation Evidence`, and attempt history in `Implementation Execution Log`. Omit optional evidence rows with no entries.

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

## Implementation Task Ledger

Use this as the single recovery view for implementation progress, current task, last safe checkpoint, and next handoff. Keep one row per task from `tasks.md`.

| Field | Value |
| --- | --- |
| Overall status | See `devspec/glossary.md#task-status-values` |
| Completed count | |
| Pending count | |
| Skipped count | |
| Current task | |
| Last completed task | |
| Last confirmation outcome | proceed, continue, pause, skip, custom |
| Known good state | |
| Roll-forward notes | |
| Completion note | |

| Task | Target repository | Target area | Depends on | Status | Attempt count | Last checkpoint | Validation last run | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 |  |  |  | pending | 0 |  |  | |

## Implementation Evidence

Record only evidence that exists. Use this section for repository access checks, changed files or changed areas, validation results, type-specific handling, residual risks, follow-ups, and review/audit snippets. Use `Changed file` for small targeted edits and `Changed area` for broad mechanical edits where listing each file would add noise. Repository path and access requirement source is `devspec/foundation/codebase-structure.md`; type-specific rule source is `devspec/foundation/rules.md`.

| Type | Applies to | Item | Evidence or notes | Status |
| --- | --- | --- | --- | --- |
| Repository access | <repository-name> | <access-requirement-and-status> | <confirmation-or-blocker-notes> | confirmed, missing, blocked |
| Changed file or area | <task-id> | <path-or-area> | <change-summary-and-validation> | modified |
| Validation | <task-id-or-scope> | <command-or-method> | <result-or-expected-signal> | pending, passed, failed, skipped |
| Type-specific handling | <bug-security-or-rule> | <handling-note> | <rule-source-or-audit-note> | pending, complete |
| Risk or follow-up | <task-id-or-work-item> | <risk-or-follow-up> | <owner-or-next-action> | open, pending, complete |
| Review snippet | <task-id-or-file> | <before-after-or-audit-summary> | <why-useful-for-review> | recorded |
| Token telemetry | <run-or-task> | before, after, unavailable | <usage-summary-or-unavailable-reason> | recorded |

## Implementation Execution Log

Record one row per task attempt, validation run, blocker, retry escalation, pause, skip, completion, or handoff. Failed methods, retry conditions, and next safer methods belong here.

| Date | Task | Event | Attempt count | Status | Summary | Evidence refs | Blockers | Failed method and reason | Retry condition or next safer method | Confirmation or handoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | T-001 | attempt, validation, blocker, retry-escalation, pause, skip, completion, handoff | 0 | pending |  |  |  |  |  |  |
