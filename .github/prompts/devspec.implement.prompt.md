---
name: "devspec.implement"
description: "Implement pending tasks for the current ready devspec work item, confirm whether to proceed after each task, and update implement.md with progress, validation, and completion summaries."
argument-hint: "Optional: add additive guidance for implementation, validation, or task-order handling"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<feature-name>/implement.md`.

Optional user input:
${input:implementInput:Optional: add additive guidance for implementation, validation, task order, or skip handling}

Execution:
- Pass optional implementation guidance to `devspec.implement-task`; the agent owns target selection, prerequisite validation, task execution, confirmations, repo access, validation, telemetry notes, artifact updates, and handoff behavior.
