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
- Validate whether the input is a supported provider URL or identifier before treating it as resolved.
- Resolve the reference when possible using the provider guidance in `devspec/foundation/provider-integrations.md`.
- If provider resolution succeeds, show at least provider, identifier, title, type when available, current external status when available, canonical link, and a short summary, then require explicit confirmation before creating or updating the work-item folder.
- Offer only these confirmation actions after successful resolution: confirm and continue, reject and retry input, switch to manual intake, or cancel.
- If the reference is ambiguous or cannot be resolved confidently, ask for clarification and stop.
- If the input format is invalid, fail fast, explain why, and ask the user to correct it or choose manual intake.
- If provider lookup is unavailable or the item cannot be resolved, do not guess. Record the attempt and offer manual intake only as an explicit fallback.
- Manual intake requires a user-provided external reference plus manual description and manual acceptance criteria before the work item can be created.
- Classify the work item as `feature`, `bug`, or `security-vulnerability`. If that classification is unclear, ask for clarification instead of guessing.
- Ask missing clarification or confirmation questions one at a time using clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's answer before asking the next question.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Create the work-item folder during the story stage and keep the folder path stable after creation.
- Write or update `meta.md` and `story.md` for the target work item.
- Record source resolution status, provider, resolution notes, and resolved item confirmation status in `meta.md`.
- Record the resolved summary shown and the confirmation actions offered in `story.md`.
- Record type, impact, affected scope, and type-appropriate urgency in `meta.md` and `story.md`.
- For features, record priority instead of severity.
- For features, confirm whether the work has multi-repo dependencies.
- If a feature has multi-repo dependencies, ask for all affected or dependent repos and record them in `meta.md` and `story.md`.
- Record the external reference in `story.md`.
- For manual intake, record the manual description and manual acceptance criteria in `story.md`.
- For bugs, capture expected behavior, actual behavior, reproduction steps, regression context, and user impact.
- For security vulnerabilities, capture severity, affected scope, vulnerability class, attack surface, exploitability, disclosure status, and containment or remediation notes.
- Minimize sensitive exploit detail in shared artifacts unless it is necessary for remediation.
- Initialize `decisions.md` and `notes.md` if the work-item folder is being created for the first time.
- Resolve missing facts through the one-question-at-a-time flow instead of leaving unresolved items whenever practical.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, key changes, questions resolved, remaining blockers if any, and the recommended next step or prompt to run.

