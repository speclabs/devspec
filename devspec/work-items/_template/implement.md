# Implementation Record

Use this artifact for implementation recovery, evidence, and handoff. Keep task targets in `tasks.md`; omit evidence rows with no entries.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | implement |
| Current command | `/devspec.implement` |
| Current agent | devspec.implement-task |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | baseline or CR-### |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Question options and examples | |
| Custom Answer entry or response | |
| Recommended option and justification | |
| Continuation condition | |
| Resume command | `/devspec.implement` |
| Resume notes | |
| Updated | |

## Implementation Task Ledger

Use this as the recovery view. Keep one row per task from `tasks.md`; source refs, scope, targets, and dependencies stay there. For change requests, append rows for the active `CR-###` and preserve prior baseline or CR rows.

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

| Task | Status | Attempt count | Last checkpoint | Task quality notes | Validation last run | Next action |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | pending | 0 |  | <actionable-or-blocker-summary> |  | |

## Implementation Evidence

Record only evidence that exists. Use `Changed file` for targeted edits and `Changed area` for broad edits. Append evidence for later `CR-###` work; do not rewrite prior baseline or CR evidence except with explicit correction notes.

| Type | Applies to | Item | Evidence or notes | Status |
| --- | --- | --- | --- | --- |
| Repository access | <repository-name> | <access-requirement-and-status> | <confirmation-or-blocker-notes> | confirmed, missing, blocked |
| Changed file | <task-id> | <path> | <change-summary-and-validation> | modified |
| Changed area | <task-id> | <area-or-glob> | <change-summary-and-validation> | modified |
| Validation | <task-id-or-scope> | <command-or-method> | <result-or-expected-signal> | pending, passed, failed, skipped |
| Type-specific handling | <bug-security-or-rule> | <handling-note> | <rule-source-or-audit-note> | pending, complete |
| Risk or follow-up | <task-id-or-work-item> | <risk-or-follow-up> | <owner-or-next-action> | open, pending, complete |
| Review snippet | <task-id-or-file> | <before-after-or-audit-summary> | <why-useful-for-review> | recorded |
| Token telemetry | <run-or-task> | before, after, unavailable | <usage-summary-or-unavailable-reason> | recorded |

## Implementation Execution Log

Record one row per task-quality check, attempt, validation, blocker, retry escalation, pause, skip, completion, or handoff. Put recovery details in `Summary` or `Next action`.

| Date | Task | Event | Attempt | Status | Summary | Evidence refs | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | T-001 | task-quality-check, attempt, validation, blocker, retry-escalation, pause, skip, completion, handoff | 0 | pending |  |  |  |
