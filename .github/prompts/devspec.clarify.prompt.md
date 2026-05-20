---
name: "devspec.clarify"
description: "Ask and record exactly one blocking clarification question at a time for the current devspec work item, then update clarify.md."
argument-hint: "Optional: answer the current blocking question or add clarifying notes"
agent: "devspec.clarify"
---

Create or update `devspec/work-items/<work-item-folder>/clarify.md` for the current work item.

Optional user input:
${input:clarifyInput:Optional: answer the current blocking question or add clarifying notes}

Execution:
- Pass optional clarification guidance to `devspec.clarify`; the agent owns target selection, prerequisite validation, one-question-at-a-time clarification, artifact updates, and handoff behavior.
