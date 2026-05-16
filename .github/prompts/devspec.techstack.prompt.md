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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/tech-stack.md`.
- Capture versions, platform constraints, tooling, and operational assumptions when known.
- Organize the artifact by project or repo, using one heading per project.
- Keep tech stack details in Markdown tables.
- Include both the version used in the project and the current market version when that information is available.
- Use web lookup when practical to identify current market versions.
- If the current market version cannot be verified, record that clearly instead of guessing.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
