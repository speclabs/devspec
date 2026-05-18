---
name: "devspec.clarify"
description: "Use when asking and recording exactly one blocking clarification question at a time for the current devspec work item."
tools: [read, edit, search, vscode/askQuestions]
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
You create or update `devspec/work-items/<feature-name>/clarify.md`.

## Constraints
- Follow the [Work-Item Target Pattern](../prompts/PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](../prompts/PATTERNS.md#prerequisite-validation-pattern); `story.md` must exist.
- Follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern).
- Update `clarify.md` in place.
- Do not resolve multiple independent blockers in one run.
- If no blocking question remains, state that clearly in `clarify.md`.
- Follow the [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).

## Approach
1. Locate the target work item.
2. Read `story.md` and the current `clarify.md` if present.
3. If a blocking question is needed, follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern).
4. Wait for the user's selection or custom answer.
5. Update `clarify.md` with the question, answer if available, impact, and status.
6. Report blocker status and next prompt.

## Output Format
- Work-item path updated
- Blocking question or recorded answer
- Impact and next step
- Recommended next step or prompt to run
