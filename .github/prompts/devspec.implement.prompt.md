name: "devspec.implement"
description: "Implement pending tasks for the current ready devspec work item, confirm whether to proceed after each task, and update implement.md with progress, validation, and completion summaries."
argument-hint: "Optional: add additive guidance for implementation, validation, or task-order handling"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<feature-name>/implement.md`.

Optional user input:
${input:implementInput:Optional: add additive guidance for implementation, validation, task order, or skip handling}

Requirements:
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `finalize.md` is missing, not `ready`, or if `tasks.md` is missing.
- Treat optional user input as additive only.
- If clarification or confirmation is required at any point, ask exactly one question at a time with clickable options whenever reasonable, include `Custom Answer`, and wait for the user's answer before continuing.
- Implement pending tasks from `tasks.md` sequentially in the current run unless the user chooses to stop or skip.
- Select the next pending task using `tasks.md` and any prior handoff recorded in `implement.md`.
- Modify code when applicable and stay within the finalized scope.
- For bugs, record regression-validation evidence in the implementation log.
- For bugs, record focused before-fix and after-fix code snippets in `implement.md` for audit purposes only.
- For security vulnerabilities, minimize sensitive exploit detail and record remediation, verification, and backport or advisory status where applicable.
- After each task, report how many tasks are completed and how many remain pending, then ask the user whether to `proceed`, `skip`, or provide a `Custom Answer` before continuing.
- If the same task enters a repair or retry loop more than 3 times, stop, explain the issue, and ask the user whether to `proceed`, `skip`, or provide a `Custom Answer` before continuing.
- Capture a token-usage summary before implementation starts and after all tasks are completed when runtime telemetry is available. If telemetry is unavailable, record that explicitly instead of inventing values.
- Record the token summary in `implement.md` as a Markdown table covering before implementation, after completion, and delta.
- Write or update `implement.md` with progress counts, task-level implementation log entries, files changed, validation performed, blockers, residual risks, type-specific handling notes, confirmation outcomes, loop-escalation notes, completed-task summaries, pending or skipped task summaries, token-usage summary, and the next-task handoff when applicable.
- If code changes are not applicable in the current repository, record that clearly in `implement.md`.
- If no pending task remains, update `implement.md` to show the completed task list and a completion summary, then notify the user that all planned tasks are already implemented.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, tasks completed, tasks pending or skipped, implementation status, validation outcome, confirmation outcomes, token-usage summary availability, and the recommended next step or prompt to run.