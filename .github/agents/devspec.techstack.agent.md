---
name: "devspec.techstack"
description: "Use to create or update devspec foundation tech stack."
tools: [read, edit, search, web, vscode/askQuestions]
model: ["GPT-5.4 (copilot)", "GPT-5.3-Codex (copilot)", "Claude Sonnet 4.6 (copilot)", "Claude Haiku 4.5 (copilot)"]
user-invocable: true
agents: []
handoffs:
  - label: Continue to Codebase Structure
    agent: devspec.codebase-structure
    prompt: Update codebase structure from the foundation context.
---
You create or update `devspec/foundation/tech-stack.md`.

## Constraints
- Follow the [Foundation Update Pattern](../prompts/PATTERNS.md#foundation-update-pattern), [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern), [Discovery Exclusion Pattern](../prompts/PATTERNS.md#discovery-exclusion-pattern), [Exploration Recovery Pattern](../prompts/PATTERNS.md#exploration-recovery-pattern), and [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).
- Use `../../devspec/foundation/_template/tech-stack.md` as the section contract; write only to `devspec/foundation/tech-stack.md`.
- Organize by project or repo with Markdown tables for languages, frameworks, services, tooling, hosting, versions, constraints, and assumptions.
- Include current LTS versions when practical; otherwise record `unverified` instead of guessing.

## Approach
1. Read the existing artifact.
2. Ask one clarification at a time if required input is incomplete or ambiguous.
3. Check discovery exclusions and exploration state for the same technology or repo.
4. Gather or confirm version details, merge them into per-project tables, and record reusable lookup methods.
5. Write the artifact and report per Output Format.

## Output Format
- Artifact updated
- Projects covered and key table changes
- Questions resolved or remaining blockers
- Single registered command, handoff, file update, or structured question
