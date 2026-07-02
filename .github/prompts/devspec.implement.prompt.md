---
name: "devspec.implement"
description: "Implement pending tasks for the current ready work item, confirm after each task, and update structured implement.md checkpoints."
argument-hint: "Optional: add implementation, validation, task-order, or skip guidance"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<work-item-folder>/implement.md` with implementation task ledger state, implementation evidence, execution history, blockers, and handoff notes. Keep `tasks.md#implementation-tasks` status, attempt count, and checkpoint fields aligned with implementation progress.

For accepted post-baseline change requests, follow the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern) and append CR-scoped evidence without rewriting prior baseline or CR evidence.

Apply the [Minimum Necessary Implementation Pattern](PATTERNS.md#minimum-necessary-implementation-pattern) before each task attempt, including confirming whether the task requires a code change and keeping evidence focused on actual access checks, changes, validation, blockers, risks, retries, and handoff details.

Apply the [Task Quality Gate Pattern](PATTERNS.md#task-quality-gate-pattern) before each task attempt.

Optional user input:
${input:implementInput:Optional: add implementation, validation, task-order, or skip guidance}
