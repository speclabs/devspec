---
name: "devspec.tasks"
description: "Create or update ordered implementation tasks for the current ready devspec work item and record them in tasks.md."
argument-hint: "Optional: add additive guidance for task decomposition"
agent: "devspec.tasks"
---

Create or update `devspec/work-items/<feature-name>/tasks.md` for the current work item.

Optional user input:
${input:tasksInput:Optional: add additive guidance for task decomposition}

Requirements:
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `finalize.md` is missing or not marked `ready`.
- Treat optional user input as additive only.
- Do not change or expand the finalized scope.
- Write or update `tasks.md` with ordered tasks, dependencies, likely impacted files or components, validation steps, and definition of done.
- Summarize the work-item path updated, key task groups, and any blocker.
