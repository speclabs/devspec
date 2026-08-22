---
name: "devspec.changerequest"
description: "Append one missed related requirement to a finalized work item without rewriting baseline history."
argument-hint: "Enter the existing work item and one missing description, acceptance criterion, requirement, quality constraint, or edge case"
agent: "devspec.changerequest"
---

Record one missed, related completeness addition for an existing work item whose status is `finalized`, `tasks-planned`, `implementing`, `implemented`, `reviewing`, or `reviewed`. Append the addition as the next `CR-###` row and CR-scoped story rows in the existing work-item artifacts; do not create a new Markdown file for the change request or rewrite baseline history.

Use this command for a missing description, acceptance criterion, functional requirement, nonfunctional requirement, or edge case that completes the same intended outcome. If the input is independent, use the structured selection required by the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern); a selected linked item continues through `/devspec.story`.

