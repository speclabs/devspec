---
name: "devspec.clarify"
description: "Ask, resolve, and record one active blocking clarification at a time for the current devspec work item."
argument-hint: "Optional: answer the active blocker or add clarifying notes"
agent: "devspec.clarify"
---

Create or update `devspec/work-items/<work-item-folder>/clarify.md` for the current work item.

Use clarification only for active blockers inside current scope. If input introduces post-baseline scope for an item whose status is `finalized`, `tasks-planned`, `implementing`, `implemented`, `reviewing`, or `reviewed`, follow the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern) and route to `/devspec.story`.

Optional user input:
${input:clarifyInput:Optional: answer the active blocker or add clarifying notes}
