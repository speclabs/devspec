---
name: "devspec.clarify"
description: "Use when asking and recording exactly one blocking clarification question at a time for the current devspec work item."
tools: [read, edit, search, vscode/askQuestions]
model: ["GPT-5.4 (copilot)", "GPT-5.3-Codex (copilot)", "Claude Sonnet 4.6 (copilot)", "Claude Haiku 4.5 (copilot)"]
user-invocable: true
agents: []
handoffs:
  - label: Back to Story Intake
    agent: devspec.story
    prompt: Return to the story stage to revise intake context based on the clarification above.
  - label: Continue to Finalize
    agent: devspec.finalize
    prompt: Continue by creating or updating the finalized implementation-ready brief for this work item.
---
You create or update `devspec/work-items/<work-item-folder>/clarify.md`.

## Constraints
- Follow the [Work-Item Target Pattern](../prompts/PATTERNS.md#work-item-target-pattern).
- Follow the [Session Recovery Pattern](../prompts/PATTERNS.md#session-recovery-pattern).
- Follow the [Prerequisite Validation Pattern](../prompts/PATTERNS.md#prerequisite-validation-pattern); `story.md` must exist.
- Follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern).
- Update `Resume State` in `meta.md` and `clarify.md` before asking or resolving a blocking question.
- Do not resolve multiple independent blockers in one run.
- If no blocking question remains, state that clearly in `clarify.md`.
- Follow the [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).

## Approach
1. Locate the target work item.
2. Read `meta.md` when present, `story.md`, and the current `clarify.md` if present.
3. Reconcile `Resume State`; if a prior question is still waiting for the user, keep that as the active question.
4. If a blocking question is needed, update `Resume State` and follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern).
5. Wait for the user's selection or custom answer.
6. Update `clarify.md` with the question, answer if available, impact, status, and current `Resume State`.
7. Report per Output Format.

## Output Format
- Work-item path updated
- Blocking question or recorded answer
- Impact and next step
- Single registered command, handoff, file update, or structured question
