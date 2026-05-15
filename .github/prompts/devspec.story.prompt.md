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
- Classify the work item as `feature`, `bug`, or `security-vulnerability`. If that classification is unclear, ask for clarification instead of guessing.
- Create the work-item folder during the story stage and keep the folder path stable after creation.
- Write or update `meta.md` and `story.md` for the target work item.
- Record type, severity, impact, and affected scope in `meta.md` and `story.md`.
- For bugs, capture expected behavior, actual behavior, reproduction steps, regression context, and user impact.
- For security vulnerabilities, capture severity, affected scope, vulnerability class, attack surface, exploitability, disclosure status, and containment or remediation notes.
- Minimize sensitive exploit detail in shared artifacts unless it is necessary for remediation.
- Initialize `decisions.md` and `notes.md` if the work-item folder is being created for the first time.
- Capture open questions explicitly instead of guessing missing facts.
- Summarize the work-item path updated, key changes, and any blocker.

