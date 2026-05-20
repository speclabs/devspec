---
name: "devspec.story"
description: "Create or update a devspec work item from a story, Jira, bug, issue, task, or PBI number, or from the full GitHub, Azure DevOps, or Jira URL."
argument-hint: "Enter a story, Jira, bug, issue, task, or PBI number, or paste the full URL"
agent: "devspec.story"
---

Create or update the work-item intake artifacts under `devspec/work-items/<work-item-folder>/`.

Required user input:
${input:workItemReference:Enter the story, Jira, bug, issue, task, or PBI number, or paste the full URL}

Execution:
- Pass the required work-item reference to `devspec.story`; the agent owns provider resolution, manual fallback, work-item folder naming, artifact creation, clarification, multi-repo handling, type-specific intake, and handoff behavior.

