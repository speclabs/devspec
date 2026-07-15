---
name: "devspec.finalize"
description: "Create or update the structured implementation readiness brief for the current devspec work item."
argument-hint: "Optional: add reviewer notes, constraints, or finalization guidance"
agent: "devspec.finalize"
---

Create or update `devspec/work-items/<work-item-folder>/finalize.md` for the current work item with generic requirement coverage and dependencies, implementation-oriented readiness, foundation and architecture alignment, implementation brief, validation plan, and blockers.

Finalize is the readiness gate before `/devspec.tasks`; apply the [Requirement Completeness Matrix Pattern](PATTERNS.md#requirement-completeness-matrix-pattern) and [Technology-Neutral Safety Baseline Pattern](PATTERNS.md#technology-neutral-safety-baseline-pattern), and mark the work item `ready` only when every applicable coverage row and readiness gate is `ready` or `not applicable`.

For accepted post-baseline change requests, follow the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern) and append CR-scoped readiness, implementation brief, and validation rows without rewriting baseline rows.

Optional user input:
${input:finalizeInput:Optional: add reviewer notes, constraints, or finalization guidance}
