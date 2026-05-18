---
name: "devspec.implement"
description: "Implement pending tasks for the current ready devspec work item, confirm whether to proceed after each task, and update implement.md with progress, validation, and completion summaries."
argument-hint: "Optional: add additive guidance for implementation, validation, or task-order handling"
agent: "devspec.implement-task"
---

Implement the current work item and update `devspec/work-items/<feature-name>/implement.md`.

Optional user input:
${input:implementInput:Optional: add additive guidance for implementation, validation, task order, or skip handling}

Requirements:
- Follow the [Work-Item Target Pattern](PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); `finalize.md` must be `ready` and `tasks.md` must exist.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) for target selection, blockers, and per-task proceed or skip decisions.
- Implement pending tasks from `tasks.md` sequentially in the current run unless the user chooses to stop or skip.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) and validate repo access before changing code for a task.
- Select the next pending task using `tasks.md` and any prior handoff recorded in `implement.md`.
- Modify code when applicable and stay within the finalized scope.
- Apply the relevant bug and security implementation rules in `devspec/foundation/rules.md`.
- After each task, report how many tasks are completed and how many remain pending, then ask the user whether to `proceed`, `skip`, or provide a `Custom Answer` before continuing.
- If the same task enters a repair or retry loop more than 3 times, stop, explain the issue, and ask the user whether to `proceed`, `skip`, or provide a `Custom Answer` before continuing.
- Capture a token-usage summary before implementation starts and after all tasks are completed when runtime telemetry is available. If telemetry is unavailable, record that explicitly instead of inventing values.
- Record the token summary in `implement.md` as a Markdown table covering before implementation, after completion, and delta.
- Write or update `implement.md` using `devspec/work-items/_template/implement.md` as the section contract.
- If code changes are not applicable in the current repository, record that clearly in `implement.md`.
- If no pending task remains, update `implement.md` to show the completed task list and a completion summary, then notify the user that all planned tasks are already implemented.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
