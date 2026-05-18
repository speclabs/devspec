---
name: "devspec.clarify"
description: "Ask and record exactly one blocking clarification question at a time for the current devspec work item, then update clarify.md."
argument-hint: "Optional: answer the current blocking question or add clarifying notes"
agent: "devspec.clarify"
---

Create or update `devspec/work-items/<feature-name>/clarify.md` for the current work item.

Optional user input:
${input:clarifyInput:Optional: answer the current blocking question or add clarifying notes}

Requirements:
- Follow the [Work-Item Target Pattern](PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); `story.md` for the target work item must exist.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern).
- Write or update `clarify.md` with the current blocking question, any answer provided, its impact, and the current status.
- If no blocking question remains, state that clearly in `clarify.md`.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
