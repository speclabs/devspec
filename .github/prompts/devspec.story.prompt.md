---
name: "devspec.story"
description: "Create or update one devspec work item, or append a related post-baseline change request."
argument-hint: "Enter one work item, provider URL or identifier, bug report, feature request, task, PBI, or change request"
agent: "devspec.story"
---

Create or update the work-item intake artifacts under `devspec/work-items/<work-item-folder>/`. Provide one story, feature, bug, security issue, task, PBI, or related post-baseline change request per run; include summary, description, acceptance criteria, requirements, edge cases, and planning signals when available. For existing work items whose status is `finalized`, `tasks-planned`, `implementing`, `implemented`, `reviewing`, or `reviewed`, follow the [Work-Item Change Request Pattern](PATTERNS.md#work-item-change-request-pattern).

Required user input:

<runtime_input>
${input:workItemReference:Enter one work item, provider URL or identifier, bug report, feature request, task, PBI, or change request}
</runtime_input>
