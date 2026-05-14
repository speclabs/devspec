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
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `story.md` for the target work item is missing.
- Ask exactly one blocking question at a time.
- Treat optional user input as additive only.
- Write or update `clarify.md` with the current blocking question, any answer provided, its impact, and the current status.
- If no blocking question remains, state that clearly in `clarify.md`.
- Summarize the work-item path updated, current blocker status, and next step.
