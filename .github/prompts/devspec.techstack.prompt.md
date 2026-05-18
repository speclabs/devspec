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
- Follow the [Foundation Update Pattern](PATTERNS.md#foundation-update-pattern).
- Organize by project or repo with Markdown tables for languages, frameworks, services, tooling, hosting, versions, constraints, and assumptions.
- Include current market versions when practical to verify; otherwise record `unverified` instead of guessing.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
