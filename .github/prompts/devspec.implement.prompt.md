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
- For bugs, record regression-validation evidence in the implementation log.
- For bugs, record focused before-fix and after-fix code snippets in `implement.md` for audit purposes only.
- For security vulnerabilities, minimize sensitive exploit detail and record remediation, verification, and backport or advisory status where applicable.
- Write or update `implement.md` with a task-level implementation log entry, files changed, validation performed, blockers, residual risks, type-specific handling notes, and the next-task handoff.
- If code changes are not applicable in the current repository, record that clearly in `implement.md`.
- If no pending task remains, update `implement.md` to show completion and notify the user that all planned tasks are already implemented.
- Do not continue into a second task in the same run unless the user explicitly asks after the first task is logged.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, the task implemented, implementation status, validation outcome, next-task handoff, and the recommended next step or prompt to run.