---
name: "devspec.implement"
description: "Implement the current ready devspec work item when applicable, then update implement.md with execution outcome and validation summary."
argument-hint: "Optional: add additive guidance for implementation or validation"
agent: "devspec.implement"
---

Implement the current work item and update `devspec/work-items/<feature-name>/implement.md`.

Optional user input:
${input:implementInput:Optional: add additive guidance for implementation or validation}

Requirements:
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `finalize.md` is missing, not `ready`, or if `tasks.md` is missing.
- Treat optional user input as additive only.
- Modify code when applicable and stay within the finalized scope.
- Write or update `implement.md` with the implementation outcome, files changed, validation performed, residual risks, and follow-up work.
- If code changes are not applicable in the current repository, record that clearly in `implement.md`.
- Summarize the work-item path updated, implementation status, and validation outcome.