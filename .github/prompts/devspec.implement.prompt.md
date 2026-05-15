---
name: "devspec.implement"
description: "Implement exactly one task at a time for the current ready devspec work item, then update implement.md with the task execution log, validation summary, and next-task handoff."
argument-hint: "Optional: add additive guidance for the next task to implement or its validation"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<feature-name>/implement.md`.

Optional user input:
${input:implementInput:Optional: add additive guidance for the next task to implement or its validation}

Requirements:
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `finalize.md` is missing, not `ready`, or if `tasks.md` is missing.
- Treat optional user input as additive only.
- Implement exactly one task from `tasks.md` per run.
- Select the next pending task using `tasks.md` and any prior handoff recorded in `implement.md`.
- Modify code when applicable and stay within the finalized scope.
- Write or update `implement.md` with a task-level implementation log entry, files changed, validation performed, blockers, residual risks, and the next-task handoff.
- If code changes are not applicable in the current repository, record that clearly in `implement.md`.
- Do not continue into a second task in the same run unless the user explicitly asks after the first task is logged.
- Summarize the work-item path updated, the task implemented, implementation status, validation outcome, and next-task handoff.