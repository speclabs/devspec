# Tasks

Use this artifact as the executable implementation plan. Keep lifecycle recovery in `Resume State`, source references in `Planning Basis`, and all executable task details in `Implementation Tasks`. Each task should include target, dependency, impacted area, validation, and done condition.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | tasks |
| Current command | `/devspec.tasks` |
| Current agent | devspec.tasks |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.tasks` |
| Resume notes | |
| Updated | |

## Planning Basis

| Field | Value |
| --- | --- |
| Implementation brief source | `finalize.md#implementation-brief` |
| Validation source | `finalize.md#validation-plan` |
| Readiness source | `finalize.md#readiness` |
| Access requirement source | `devspec/foundation/codebase-structure.md` |
| Type-specific rule source | `devspec/foundation/rules.md` |

## Implementation Tasks

Use one row per executable checkpoint. Put likely files or areas, validation steps, and done criteria on the task that owns them. Keep validation commands or methods specific enough for `implement.md` to execute or record.

| ID | Task | Target repo | Target area or files | Required access | Depends on | Validation | Done when | Status | Attempt count | Last checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | <developer-action> | <repo-name> | <path-module-or-area> | See `devspec/glossary.md#access-requirement-values` | <task-id-or-none> | <command-method-or-review-signal-and-expected-result> | <observable-completion-condition-and-evidence> | pending | 0 | |
