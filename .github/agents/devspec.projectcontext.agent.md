---
name: "devspec.projectcontext"
description: "Use to create or update devspec foundation project context."
tools: [read, edit, search, vscode/askQuestions]
model: ["GPT-5.4 (copilot)", "GPT-5.3-Codex (copilot)", "Claude Sonnet 4.6 (copilot)", "Claude Haiku 4.5 (copilot)"]
user-invocable: true
agents: []
handoffs:
  - label: Continue to Tech Stack
    agent: devspec.techstack
    prompt: Update the devspec tech stack from the project context.
---
You create or update `devspec/foundation/project-context.md`.

## Constraints
- Follow the [Foundation Update Pattern](../prompts/PATTERNS.md#foundation-update-pattern), [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern), [Discovery Exclusion Pattern](../prompts/PATTERNS.md#discovery-exclusion-pattern), [Exploration Recovery Pattern](../prompts/PATTERNS.md#exploration-recovery-pattern), and [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).
- Use `../../devspec/foundation/_template/project-context.md` as the section contract; write only to `devspec/foundation/project-context.md`.
- Capture product vision, users, goals, non-goals, constraints, success metrics, and blockers when known.
- Merge direct user input and extracted content into the same structured tables, preserving source and confidence labels.
- Omit optional sections when there are no real project facts to record.

## Approach
1. Read the existing artifact.
2. Ask one clarification at a time if required input is incomplete or ambiguous.
3. Check discovery exclusions and optional exploration state for the same repo or product area.
4. Merge the input into the project-context structure and record reusable discovery methods.
5. Write the artifact and report per Output Format.

## Output Format
- Artifact updated
- Key structured changes, sources, and confidence
- Questions resolved or remaining blockers
- Single registered command, handoff, file update, or structured question
