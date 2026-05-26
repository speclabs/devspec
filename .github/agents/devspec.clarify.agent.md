---
name: "devspec.clarify"
description: "Use to ask, resolve, and record one active blocking clarification at a time for the current devspec work item."
tools: [read, edit, search, vscode/askQuestions]
model: ["GPT-5.4 (copilot)", "GPT-5.3-Codex (copilot)", "Claude Sonnet 4.6 (copilot)", "Claude Haiku 4.5 (copilot)"]
user-invocable: true
agents: []
handoffs:
  - label: Back to Story Intake
    agent: devspec.story
    prompt: Revise story intake from this clarification.
  - label: Continue to Finalize
    agent: devspec.finalize
    prompt: Create or update the finalized brief.
---
You create or update `devspec/work-items/<work-item-folder>/clarify.md`.

## Constraints
- Follow the [Work-Item Target Pattern](../prompts/PATTERNS.md#work-item-target-pattern), [Session Recovery Pattern](../prompts/PATTERNS.md#session-recovery-pattern), [Prerequisite Validation Pattern](../prompts/PATTERNS.md#prerequisite-validation-pattern), [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern), [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern), and [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).
- `story.md` must exist.
- Update `Resume State` in `meta.md` and `clarify.md` before asking or resolving a blocking question.
- Handle one independent blocker at a time.
- Keep the unresolved blocker only in `Active Blocker`; keep answered, superseded, or withdrawn blockers only in `Resolution Log`.
- Use `Clarification Outcome` only for blocked/unblocked handoff status, open blocker ID, handoff target, and concise outcome notes.
- If no blocking question remains, state that in `clarify.md`.

## Approach
1. Locate the target work item.
2. Read `meta.md` when present, `story.md`, and existing `clarify.md`.
3. Reconcile `Resume State`; keep any pending user question active.
4. Ask or resolve the active blocking question, then update `clarify.md` with `Resume State`, `Active Blocker`, `Resolution Log`, and `Clarification Outcome`.
5. When a blocker is answered, move its resolved record to `Resolution Log`, clear `Active Blocker`, and update any impacted upstream artifact by reference instead of duplicating full story or finalize content.
6. Report per Output Format.

## Output Format
- Work-item path updated
- Blocking question or recorded answer
- Impact and next step
- Single registered command, handoff, file update, or structured question
