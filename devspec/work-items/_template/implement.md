# Implementation Record

Use this artifact for implementation recovery, evidence, and handoff. Keep task targets in `tasks.md`; omit evidence rows with no entries.

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

Use this as the implementation recovery view. Keep one row per task from `tasks.md`; target repository, area, and dependency details stay in `tasks.md`.

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

| Task | Status | Attempt count | Last checkpoint | Validation last run | Next action |
| --- | --- | --- | --- | --- | --- |
| T-001 | pending | 0 |  |  | |

## Implementation Evidence

Record only evidence that exists. Use `Changed file` for targeted edits and `Changed area` for broad mechanical edits. Repository access source is `devspec/foundation/codebase-structure.md`; type-specific rule source is `devspec/foundation/rules.md`.

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

Record one row per task attempt, validation run, blocker, retry escalation, pause, skip, completion, or handoff. Put blockers, failed method/reason, retry condition, safer method, confirmation, or handoff in `Summary` or `Next action`.

| Date | Task | Event | Attempt | Status | Summary | Evidence refs | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | T-001 | attempt, validation, blocker, retry-escalation, pause, skip, completion, handoff | 0 | pending |  |  |  |
