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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); `finalize.md` must exist and be marked `ready`.
- Treat optional user input as additive only.
- Do not change or expand the finalized scope.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) and assign each task to a configured repo.
- Apply the relevant bug and security planning rules in `devspec/foundation/rules.md`.
- Write or update `tasks.md` with ordered tasks, repo assignments, dependencies, likely impacted files or components, validation steps, type-specific checks, and definition of done.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
