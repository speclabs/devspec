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
- For multi-repo work, assign each task to a target repo from the repo configuration recorded in `devspec/foundation/codebase-structure.md`.
- If required repo assignment is missing, or if multi-repo configuration is missing from `devspec/foundation/codebase-structure.md`, surface that as a blocker instead of guessing.
- For bugs, include reproduce, fix, and regression-validation tasks where applicable.
- For security vulnerabilities, include impact confirmation, remediation, verification across affected supported versions, and backport, release, or advisory tasks where applicable.
- Write or update `tasks.md` with ordered tasks, repo assignments, dependencies, likely impacted files or components, validation steps, type-specific checks, and definition of done.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, key task groups, any blocker, and the recommended next step or prompt to run.
