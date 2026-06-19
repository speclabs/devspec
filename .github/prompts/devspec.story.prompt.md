---
name: "devspec.story"
description: "Create or update one devspec work item from a provider URL, identifier, or manual intake."
argument-hint: "Enter one work item, provider URL or identifier, bug report, feature request, task, or PBI"
agent: "devspec.story"
---

Create or update the work-item intake artifacts under `devspec/work-items/<work-item-folder>/`. Provide one story, feature, bug, security issue, task, or PBI per run; include summary, description, acceptance criteria, requirements, edge cases, and planning signals when available.

Required user input:
${input:workItemReference:Enter one work item, provider URL or identifier, bug report, feature request, task, or PBI}
