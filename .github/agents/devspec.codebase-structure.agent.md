---
name: "devspec.codebase-structure"
description: "Use when creating or updating devspec foundation codebase structure for repository layout, module boundaries, ownership seams, and integration boundaries."
tools: [read, edit, search, vscode/askQuestions]
user-invocable: true
agents: []
handoffs:
  - label: Continue to Coding Standards
    agent: devspec.coding-standards
    prompt: Continue by creating or updating the devspec coding standards using the foundation context above.
---
You create or update `devspec/foundation/codebase-structure.md`.

## Constraints
- Follow the [Foundation Update Pattern](../prompts/PATTERNS.md#foundation-update-pattern).
- Use `../../devspec/foundation/_template/codebase-structure.md` as the section contract, but write only to `devspec/foundation/codebase-structure.md`.
- Focus on repo and module structure, not broader system architecture.
- Keep repository layout in selective 3-5 level tree-node format focused on file-placement decisions; include important source roots, feature/module folders, tests, scripts, config, infrastructure, docs, and routing-critical files when relevant.
- For multi-repo input, use one heading and one tree block per repo.
- For multi-repo configuration, capture each repo's role, local path, current workspace availability, and access requirement.
- Treat repos outside the current repo folder as valid multi-repo candidates; do not downgrade them to `reference-only` because of their location.
- Never assume `reference-only` or any other access requirement. If a repo access requirement is missing or ambiguous, ask one repo-specific multiple-choice confirmation before writing that row.
- Follow the [Multi-Repo Validation Pattern](../prompts/PATTERNS.md#multi-repo-validation-pattern) when the input spans multiple repos.
- Follow the [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern).
- Follow the [Discovery Exclusion Pattern](../prompts/PATTERNS.md#discovery-exclusion-pattern) before repository layout search or helper commands.
- Follow the [Exploration Recovery Pattern](../prompts/PATTERNS.md#exploration-recovery-pattern) before repeated repository layout search or helper commands.
- Follow the [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).

## Approach
1. Read the existing artifact if it exists.
2. Ask one clarification at a time if required input is incomplete or ambiguous, including one multiple-choice access requirement confirmation per repo when needed.
3. Check `devspec/foundation/discovery-exclusions.md` and `devspec/foundation/exploration-state.md` for exclusions plus known working or failed repository layout discovery methods for the same repo.
4. Merge the required user input into a stable codebase-structure document, keeping repository layout sections in selective 3-5 level tree-node format with one heading per repo and user-confirmed access requirements for multi-repo configuration.
5. Record meaningful working and failed layout discovery methods in `exploration-state.md`.
6. Write the updated artifact.
7. Report key changes, blockers, skipped known failed methods, and one next action or structured question.

## Output Format
- Artifact updated
- Key changes, including repo headings and tree sections updated
- Discovery exclusions applied, if material
- Skipped known failed methods, if any
- Questions resolved or remaining blockers
- Single recommended next step or structured question
