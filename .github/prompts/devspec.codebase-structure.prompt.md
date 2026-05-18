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
- Follow the [Foundation Update Pattern](PATTERNS.md#foundation-update-pattern).
- Focus on repo and module structure, not broad system architecture.
- Keep repository layout in tree-node format; for multi-repo input, use one heading and one tree block per repo.
- Follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) when the input spans multiple repos.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
