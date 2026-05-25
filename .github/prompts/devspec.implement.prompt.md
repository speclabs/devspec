---
name: "devspec.implement"
description: "Implement pending tasks for the current ready work item, confirm after each task, and update implement.md."
argument-hint: "Optional: add implementation, validation, task-order, or skip guidance"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<work-item-folder>/implement.md`.

Optional user input:
${input:implementInput:Optional: add implementation, validation, task-order, or skip guidance}
