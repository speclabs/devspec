# Glossary

Use this file for shared devspec terms and status values.

Status values are scoped. Use a value only in the table named by the consuming artifact. When the same literal appears in more than one table, its meaning is limited to that table's context.

## Workflow State Values

Use these values to track command recovery, work-item lifecycle, and task execution. Do not use workflow state values as review or readiness decisions.

### Run Status Values

Use for the current command or agent run in a `Resume State` or `Workflow State` table.

| Status | Meaning |
| --- | --- |
| `active` | Work is in progress. |
| `waiting-for-user` | Work is paused until the user answers a recorded question. |
| `paused` | Work is intentionally paused and can resume from the recorded state. |
| `stopped` | Work stopped without an active resume path. |
| `blocked` | Required evidence, access, or context is missing. |
| `complete` | The stage or run is finished. |

### Work-Item Status Values

Use for the durable lifecycle of a work item in `meta.md`. Readiness, review outcomes, blockers, and run interruptions are recorded in their own fields or artifacts, not encoded into the work-item status.

| Status | Meaning |
| --- | --- |
| `intake` | Initial work-item capture is in progress. |
| `clarifying` | The item needs user or source clarification. |
| `finalized` | Scope is captured; readiness status records whether task planning may proceed. |
| `tasks-planned` | Implementation tasks are recorded. |
| `implementing` | Implementation is in progress. |
| `implemented` | Implementation is complete and awaiting review. |
| `reviewing` | Review is in progress. |
| `reviewed` | Review is complete. |

### Task Status Values

Use for executable implementation tasks and implementation task ledgers.

| Status | Meaning |
| --- | --- |
| `pending` | Not started. |
| `active` | In progress. |
| `paused` | Paused mid-task. |
| `blocked` | Cannot proceed until a blocker is resolved. |
| `complete` | Finished. |
| `skipped` | Intentionally not performed. |

## Decision Values

Use these values for gates and outcomes. They are decisions, not workflow progress markers.

### Readiness Status Values

Use for requirement coverage rows, readiness gates, and the overall readiness field. Overall readiness uses only `ready` or `not ready`; individual coverage and gate rows may use `not applicable` when the requirement dimension or gate does not apply.

| Status | Meaning |
| --- | --- |
| `ready` | The requirement coverage row or readiness gate has sufficient confirmed evidence for planning. |
| `not ready` | Required information, approval, access, evidence, or dependency resolution is missing. |
| `not applicable` | The requirement dimension or readiness gate does not apply to the current work-item scope. |

### Review Status Values

Use only for review outcomes.

| Status | Meaning |
| --- | --- |
| `approved` | Review found no required changes. |
| `approved-with-follow-ups` | Review passed with non-blocking follow-ups. |
| `changes-requested` | Review requires implementation changes. |

### Source Resolution Status Values

Use for intake provenance in `meta.md`.

| Status | Meaning |
| --- | --- |
| `resolved` | External source was found and confirmed. |
| `manual` | User chose manual intake without external resolution. |
| `blocked` | Source resolution is required but unavailable or invalid. |

### Change Request Disposition Values

Use for post-baseline scope changes recorded in `story.md#change-requests`. These values describe the handling decision for a requested scope change, not workflow progress.

| Status | Meaning |
| --- | --- |
| `accepted` | The request is related to the current work item, or the user explicitly confirmed appending it, and it will be tracked as CR-scoped intake, finalization, tasks, implementation, and review evidence. |
| `rejected` | The request will not be included in the current work item. |
| `superseded` | A later change request or linked work item replaces this request. |
| `withdrawn` | The requester withdrew the change request before implementation or review closure. |

### Artifact Status Values

Use for generated or queued devspec artifacts, including architecture diagram queue rows.

| Status | Meaning |
| --- | --- |
| `proposed` | Candidate identified from evidence. |
| `confirmed` | User approved generation, not yet generated. |
| `generated` | Artifact was added to the target location. |
| `skipped` | User declined generation. |
| `blocked` | Evidence or context is insufficient. |

## Access Values

### Access Requirement Values

Use for repository access requirements in `devspec/foundation/codebase-structure.md` and task rows. Access values describe the allowed interaction with a repository; they are permissions for repository use, not task or run statuses. When a task needs more access than the repository value allows, stop and ask before changing scope.

| Value | Meaning |
| --- | --- |
| `reference-only` | Read or search the repository for context only; do not edit files, run validation, or treat the repository as a delivery target. |
| `edit` | File changes are allowed in this repository, but validation is not confirmed here; record any needed validation as a separate task, handoff, or blocker. |
| `edit-and-test` | File changes and validation commands are allowed in this repository; use for normal implementation targets where the agent may both modify and verify. |
| `validation-only` | Validation commands or manual checks are allowed, but file changes are not; use for smoke tests, compatibility checks, or downstream verification repos. |
| `release-coordination` | Track release, deployment, advisory, backport, or dependency coordination for this repository; do not edit or validate it without separate confirmation. |
| `unavailable` | The repository is required but cannot currently be accessed or used; record the impact as a blocker and do not rely on this repository until access is restored. |
