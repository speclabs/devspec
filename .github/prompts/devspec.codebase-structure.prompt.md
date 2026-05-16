---
name: "devspec.codebase-structure"
description: "Create or update devspec foundation codebase structure from required user-provided repository layout, module boundaries, ownership seams, integration boundaries, and multi-repo configuration when applicable."
argument-hint: "Describe the repository layout, module boundaries, ownership seams, integration boundaries, and multi-repo configuration when applicable"
agent: "devspec.codebase-structure"
---

Create or update `devspec/foundation/codebase-structure.md`.

Required user input:
${input:codebaseStructureInput:Describe the repository layout, module boundaries, ownership seams, and integration boundaries}

Requirements:
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/codebase-structure.md`.
- Focus on repo and module structure, not broad system architecture.
- Keep repository layout output in tree node format.
- For multi-repo inputs, use one heading per repo and include one tree node block under each repo heading.
- Follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) when the input spans multiple repos.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).