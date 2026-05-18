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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Validate whether the input is a supported provider URL or identifier before treating it as resolved.
- Resolve the reference when possible using the provider guidance in `devspec/foundation/provider-integrations.md`.
- Use `devspec/foundation/provider-integrations.md` for confirmation fields, allowed confirmation actions, manual fallback, and source-resolution status.
- If the reference is ambiguous or cannot be resolved confidently, ask for clarification instead of guessing.
- If provider lookup is unavailable or the item cannot be resolved, do not guess. Record the attempt and offer manual intake only as an explicit fallback.
- Manual intake requires a user-provided external reference plus manual description and manual acceptance criteria before the work item can be created.
- Classify the work item as `feature`, `bug`, or `security-vulnerability`. If that classification is unclear, ask for clarification instead of guessing.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) for missing clarification or confirmation questions.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Create the work-item folder during the story stage and keep the folder path stable after creation.
- Write or update `meta.md` and `story.md` using the work-item templates as the section contracts.
- Record source resolution, confirmation, type, impact, affected scope, and type-appropriate urgency; for features, record priority instead of severity.
- Confirm whether the work has multi-repo dependencies and record all affected or dependent repos in `meta.md` and `story.md`.
- Follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) for multi-repo work. If configuration is missing or outdated, stop and direct the user to update `/devspec.codebase-structure` before continuing.
- Record the external reference, and for manual intake record the manual description and acceptance criteria.
- For bugs and security vulnerabilities, capture the type-specific facts required by `devspec/foundation/rules.md`.
- Initialize `decisions.md` and `notes.md` if the work-item folder is being created for the first time.
- Resolve missing facts through the one-question-at-a-time flow instead of leaving unresolved items whenever practical.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).

