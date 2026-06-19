---
name: "devspec.implement"
description: "Implement pending tasks for the current ready work item, confirm after each task, and update structured implement.md checkpoints."
argument-hint: "Optional: add implementation, validation, task-order, or skip guidance"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<work-item-folder>/implement.md` with implementation task ledger state, implementation evidence, execution history, blockers, and handoff notes.

Apply the [Minimum Necessary Implementation Pattern](PATTERNS.md#minimum-necessary-implementation-pattern) before each task attempt, including confirming whether the task requires a code change and keeping evidence focused on actual access checks, changes, validation, blockers, risks, retries, and handoff details.

Optional user input:
${input:implementInput:Optional: add implementation, validation, task-order, or skip guidance}
