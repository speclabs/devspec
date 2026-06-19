---
name: "devspec.finalize"
description: "Create or update the structured implementation readiness brief for the current devspec work item."
argument-hint: "Optional: add reviewer notes, constraints, or finalization guidance"
agent: "devspec.finalize"
---

Create or update `devspec/work-items/<work-item-folder>/finalize.md` for the current work item with implementation-oriented readiness, foundation and architecture alignment, implementation brief, validation plan, and blockers.

Finalize is the readiness gate before `/devspec.tasks`; mark the work item `ready` only when scope, acceptance criteria, repository readiness, applicable foundation constraints, architecture constraints, delivery gates, and validation expectations are clear enough to plan safely.

Optional user input:
${input:finalizeInput:Optional: add reviewer notes, constraints, or finalization guidance}
