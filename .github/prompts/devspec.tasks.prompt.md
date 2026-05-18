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
- Follow the [Work-Item Target Pattern](PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); `finalize.md` must exist and be marked `ready`.
- Do not change or expand the finalized scope.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) and assign each task to a configured repo.
- Apply the relevant bug and security planning rules in `devspec/foundation/rules.md`.
- Write or update `tasks.md` using `devspec/work-items/_template/tasks.md` as the section contract.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
