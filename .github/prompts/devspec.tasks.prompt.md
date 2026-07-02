---
name: "devspec.tasks"
description: "Create or update ordered executable implementation tasks for the current ready devspec work item."
argument-hint: "Optional: add task decomposition guidance"
agent: "devspec.tasks"
---

Create or update `devspec/work-items/<work-item-folder>/tasks.md` for the current work item with planning basis and executable implementation tasks.

Apply the [Minimum Necessary Implementation Pattern](PATTERNS.md#minimum-necessary-implementation-pattern): keep tasks scoped to the finalized brief, merge checkpoints that target the same area and validation surface, and avoid standalone refactor, dependency, abstraction, cleanup, or future-proofing tasks unless `finalize.md` requires them.

Apply the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern) for accepted post-baseline change requests: append CR-scoped task rows after the highest existing task ID and preserve completed baseline rows.

Apply the [Task Quality Gate Pattern](PATTERNS.md#task-quality-gate-pattern) before handing off to implementation.

Optional user input:
${input:tasksInput:Optional: add task decomposition guidance}
