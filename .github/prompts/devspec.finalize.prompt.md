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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required upstream artifacts must exist before finalization.
- Treat optional user input as additive only.
- If blockers remain, mark the brief as `not ready`.
- Do not invent missing requirements.
- Apply the relevant readiness gates in `devspec/foundation/rules.md` for bugs and security vulnerabilities.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) and record only the configuration status in `finalize.md`.
- For single-repo work, do not add multi-repo configuration status.
- Write or update `finalize.md` with work-item classification, readiness gates, final scope, confirmed acceptance criteria, assumptions, dependencies, multi-repo configuration status when applicable, risks, mitigations, validation approach, release or advisory needs, and ready status.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
