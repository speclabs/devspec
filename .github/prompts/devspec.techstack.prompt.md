---
name: "devspec.techstack"
description: "Create or update devspec foundation tech stack from required user-provided languages, frameworks, services, tooling, hosting, and delivery constraints."
argument-hint: "Describe the languages, frameworks, services, tooling, hosting, and delivery constraints"
agent: "devspec.techstack"
---

Create or update `devspec/foundation/tech-stack.md`.

Required user input:
${input:techStackInput:Describe the languages, frameworks, services, tooling, hosting, and delivery constraints}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Write or update `devspec/foundation/tech-stack.md`.
- Capture versions, platform constraints, tooling, and operational assumptions when known.
- Update the file in place if it already exists.
- Summarize the file updated, key changes, and open questions.
