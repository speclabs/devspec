---
name: "devspec.story"
description: "Create a development story from a story, Jira, bug, issue, task, or PBI number, or from the full GitHub, Azure DevOps, or Jira URL."
argument-hint: "Enter a story, Jira, bug, issue, task, or PBI number, or paste the full URL"
agent: "agent"
---

Create a well-structured development story from the user's work item reference below.

User input:
${input:workItemReference:Enter the story, Jira, bug, issue, task, or PBI number, or paste the full URL}

The input can be any one of the following:
- Story number
- Jira number
- Bug number
- Issue number
- Task number
- PBI number
- Full GitHub issue URL
- Full Azure DevOps work item URL
- Full Jira issue URL

Requirements:
- Interpret the input as a work item identifier or URL.
- Summarize the problem and the intended user outcome.
- Define the scope, assumptions, and constraints.
- Write clear, testable acceptance criteria.
- Call out dependencies, risks, and open questions.
- Keep the result concise and implementation-ready.

Output format:
# Story
## Summary
## Acceptance Criteria
## Constraints
## Risks
## Open Questions
