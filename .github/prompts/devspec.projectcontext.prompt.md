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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/project-context.md`.
- Keep the artifact concise, structured, and durable for later stages.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
