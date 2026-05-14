---
name: "devspec.finalize"
description: "Create or update the implementation-ready finalized brief for the current devspec work item and record it in finalize.md."
argument-hint: "Optional: add reviewer notes, constraints, or additive guidance for finalization"
agent: "devspec.finalize"
---

Create or update `devspec/work-items/<feature-name>/finalize.md` for the current work item.

Optional user input:
${input:finalizeInput:Optional: add reviewer notes, constraints, or additive guidance for finalization}

Requirements:
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if required upstream artifacts are missing.
- Treat optional user input as additive only.
- If blockers remain, mark the brief as `not ready`.
- Do not invent missing requirements.
- Write or update `finalize.md` with final scope, confirmed acceptance criteria, assumptions, dependencies, risks, mitigations, validation approach, and ready status.
- Summarize the work-item path updated, readiness status, and any blocker.
