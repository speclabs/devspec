---
name: "devspec.story"
description: "Create or update a devspec work item from a story, Jira, bug, issue, task, or PBI number, or from the full GitHub, Azure DevOps, or Jira URL."
argument-hint: "Enter a story, Jira, bug, issue, task, or PBI number, or paste the full URL"
agent: "devspec.story"
---

Create or update the work-item intake artifacts under `devspec/work-items/<feature-name>/`.

Required user input:
${input:workItemReference:Enter the story, Jira, bug, issue, task, or PBI number, or paste the full URL}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Resolve the reference when possible.
- If the reference is ambiguous or cannot be resolved confidently, ask for clarification and stop.
- Create the work-item folder during the story stage and keep the folder path stable after creation.
- Write or update `meta.md` and `story.md` for the target work item.
- Initialize `decisions.md` and `notes.md` if the work-item folder is being created for the first time.
- Capture open questions explicitly instead of guessing missing facts.
- Summarize the work-item path updated, key changes, and any blocker.

