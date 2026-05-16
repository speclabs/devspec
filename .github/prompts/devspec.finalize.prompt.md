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
- Bugs are not `ready` if reproducible behavior, user impact, or regression expectations remain unclear.
- Security vulnerabilities are not `ready` if severity, affected scope, containment or remediation plan, or validation and backport expectations are missing.
- Multi-repo work is not `ready` for implementation if required repo configuration is missing from `devspec/foundation/codebase-structure.md` or if required repo paths or workspace availability remain unknown there.
- Do not invent missing requirements.
- For multi-repo work, verify that `devspec/foundation/codebase-structure.md` contains the required repo configuration and record only the configuration status in `finalize.md`.
- For single-repo work, do not add multi-repo configuration status.
- Write or update `finalize.md` with work-item classification, readiness gates, final scope, confirmed acceptance criteria, assumptions, dependencies, multi-repo configuration status when applicable, risks, mitigations, validation approach, release or advisory needs, and ready status.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, readiness status, any blocker, and the recommended next step or prompt to run.
