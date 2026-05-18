---
name: "devspec.projectcontext"
description: "Create or update devspec foundation project context from required user-provided product vision, users, goals, non-goals, and business constraints."
argument-hint: "Describe the product vision, users, goals, non-goals, and business constraints"
agent: "devspec.projectcontext"
---

Create or update `devspec/foundation/project-context.md`.

Required user input:
${input:projectContextInput:Describe the product vision, users, goals, non-goals, and business constraints}

Requirements:
- Follow the [Foundation Update Pattern](PATTERNS.md#foundation-update-pattern).
- Capture product vision, users, goals, non-goals, constraints, success metrics, and blockers when known.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
