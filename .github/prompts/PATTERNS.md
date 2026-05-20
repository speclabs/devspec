# Shared Prompt Patterns

Use this file to keep repeated workflow behavior out of individual prompt and agent contracts.

## Interactive Question Pattern

- Ask exactly one blocking clarification, confirmation, or selection question at a time.
- Use clickable multiple-choice options whenever reasonable; for confirmations and workflow decisions, explicit options are required.
- Always include a `Custom Answer` option.
- Recommend exactly one option with a short justification.
- Do not ask open-ended confirmation questions such as "Do you want..." or "Would you like..." without explicit selectable options.
- Use `Yes`, `No`, and `Custom Answer` for binary confirmations.
- Use `Proceed`, `Skip`, and `Custom Answer` for workflow continuation, queue processing, task continuation, generated artifact approval, or retry decisions.
- Use `Continue`, `Pause`, `Skip`, and `Custom Answer` when resuming a run from `stopped` or ambiguous state.
- Use domain-specific option sets only when the stage defines them, such as provider intake actions or multi-repo access requirement values.
- Wait for the user's answer before asking the next question.
- Do not bundle unrelated questions into one message.
- If multiple confirmations are discovered at once, present only the highest-priority one and defer the rest until after the user answers.

## Next Action Selection Pattern

- The recommended next step must be singular.
- Do not output multiple next prompts, alternative command lists, or peer next-action bullets when any clarification, confirmation, queue item, handoff, retry, or fallback decision is pending.
- When multiple next actions are possible, pick the highest-priority unresolved action for the current stage and ask exactly one structured question using the [Interactive Question Pattern](#interactive-question-pattern).
- If no confirmation or selection is pending, provide exactly one recommended registered slash command, handoff, file update, or structured question.
- For queues, select the next unresolved item by the queue order and status unless the stage defines a stricter priority; do not ask the user to choose among multiple queued items unless the queue order is ambiguous.
- A final response may summarize completed work, but its action close must be one next action or one structured question.

## Registered Command Recommendation Pattern

- Use `.github/prompts/README.md#registered-slash-commands` as the canonical command registry.
- Agents must recommend only slash commands listed in the canonical command registry.
- Do not invent slash commands from natural workflow names, artifact names, queue names, or agent names.
- Do not recommend unregistered commands such as `/devspec.plan`, `/devspec.architecture`, `/devspec.provider-integrations`, `/devspec.queue`, or `/devspec.decisions`.
- Before outputting a slash command recommendation, verify that it is in the registered command list and that the matching `.github/prompts/devspec.<command>.prompt.md` file exists.
- If no registered command fits, recommend a concrete file update, a configured handoff, or a structured question instead of a slash command.
- Map common workflow labels to registered commands when appropriate: planning maps to `/devspec.tasks`, implementation maps to `/devspec.implement`, review maps to `/devspec.review`, diagram generation maps to `/devspec.diagram`, and provider integration changes map to manual updates in `devspec/foundation/provider-integrations.md`.

## Prerequisite Validation Pattern

- Validate required user input and required upstream artifacts before producing output.
- If a required prerequisite is missing, invalid, ambiguous, or not ready, stop immediately, explain the blocker, and direct the user to the correct recovery step.
- Record unresolved blockers only when the user declines to answer or the evidence remains unavailable.
- Treat optional user input as additive guidance only unless the stage explicitly requires user input.

## Session Recovery Pattern

- Treat Git-tracked `devspec` artifacts as the source of truth. Chat history and session memory are helpful but not canonical.
- At the start of every applicable command, read the target artifact and durable state files when present, then reconcile any `Resume State` sections before acting.
- Use work-item folders as the orchestration boundary. Use tasks, target repos, target areas, and attempts as execution checkpoints inside the work item.
- For monorepos, record the target repo once and distinguish tasks by module, layer, or area. For multi-repo work, every executable task must name the target repo and required access.
- Keep `Run status` values limited to `active`, `waiting-for-user`, `paused`, `stopped`, `blocked`, and `complete`.
- Use `paused` when the user expects to continue from the same task or question. Use `stopped` when the run was intentionally ended and should ask one continuation question before work resumes.
- Use `blocked` only when evidence, access, or prerequisites are insufficient. Record the blocker and the concrete condition that would allow continuation.
- Before asking any blocking question, writing a handoff, stopping after a retry loop, or ending a run, update `Resume State` with the current stage, current item, last completed step, pending question, recommended option, resume command, and next required action.
- On rerun, resume a `paused` item directly from the recorded current item when prerequisites still hold. For `stopped` or ambiguous state, ask one structured continuation question before doing more work.
- Retry only when the recorded retry condition is met, the user gives custom direction, or the method has materially changed. Do not replay known failed methods just because the session changed.
- When all tasks or queue items for the stage are complete, mark the stage `complete` and hand off to the next registered command or configured agent.

## Output Closure Pattern

- Follow the [Next Action Selection Pattern](#next-action-selection-pattern).
- Follow the [Registered Command Recommendation Pattern](#registered-command-recommendation-pattern) before recommending any slash command.
- End with exactly one registered command, handoff, file update, or structured question.
- If the next step requires user confirmation, selection, retry approval, queue approval, or workflow continuation, ask one structured question with explicit options instead of listing possible next prompts.
- Summarize only the artifact or work-item path updated, the key outcome, blockers or open questions, and the single next action.

## Token Stewardship Pattern

- Prefer canonical references over restating policy, templates, or provider rules.
- Keep stage artifacts concise: record decisions, evidence, blockers, validation, and handoffs; omit narrative filler.
- Do not duplicate content already captured in another devspec artifact. Link or name the source instead.
- Preserve user-authored content with targeted edits instead of whole-file rewrites.

## Discovery Exclusion Pattern

- Before repository search, extraction, code-pattern discovery, layout mapping, validation-surface discovery, or generated helper scripts, read `devspec/foundation/discovery-exclusions.md` when present.
- Exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output folders by default. Do not infer project conventions from installed dependency or generated output source.
- Use manifests, lockfiles, and framework config files to understand dependencies and tooling; inspect dependency folders only when the user explicitly asks or a recorded project override permits it.
- Respect repository ignore files such as `.gitignore` as a baseline, but still apply this pattern because search tools may not honor every generated or dependency path consistently.
- Apply ecosystem-specific exclusions when matching manifests or config files are present:
  - Node, Angular, React, Next, Vite: `node_modules/`, `.angular/`, `.next/`, `.turbo/`, `.vite/`, `dist/`, `build/`, `coverage/`.
  - .NET: `bin/`, `obj/`, `TestResults/`, `artifacts/`.
  - Java, Maven, Gradle: `target/`, `build/`, `.gradle/`, `out/`.
  - Python: `.venv/`, `venv/`, `env/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `site-packages/`.
  - Rust: `target/`.
  - Go: module cache and generated `vendor/` content unless the repo intentionally owns vendored source.
- Keep source discovery focused on project-owned source roots, tests, scripts, config, infrastructure, docs, manifests, and routing-critical files.
- Record project-specific include or exclude exceptions in `devspec/foundation/discovery-exclusions.md`, not in individual stage artifacts.

## Exploration Recovery Pattern

- When `.github/skills/exploration-recovery/SKILL.md` is available, use it as the operational procedure for this pattern.
- Before broad search, generated scripts, helper commands, provider lookup, or repeated discovery, follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern), then check `devspec/foundation/exploration-state.md` and session memory for known working and failed methods in the same scope.
- Use known working methods first when the scope and goal match.
- Skip known failed methods unless the user says the environment changed, the input changed, credentials changed, dependencies were installed, or the command was corrected.
- Prefer built-in repository search, targeted file reads, manifest inspection, and configured provider tools before generating broad helper scripts.
- Limit probing to one new generated script, helper command, provider lookup path, or expensive search strategy per source or goal before falling back to direct search/read evidence gathering.
- When a fallback succeeds after a failed method, record the scope, goal, failed method, failure reason, working method, and retry condition in `devspec/foundation/exploration-state.md`; optionally mirror a concise transient summary in `/memories/session/<stage>.md`.
- On rerun, use the recorded working method first and mention skipped known failures in the output.

## Foundation Update Pattern

- Required user input is mandatory.
- Ask one clarification at a time when required details are missing or ambiguous, following the Interactive Question Pattern.
- Use the matching `devspec/foundation/_template/*.md` or `devspec/architecture/_template/*.md` file as the section contract when one exists.
- Treat live `devspec/foundation/*.md` and `devspec/architecture/*.md` files as project-owned artifacts; update them in place and never replace them wholesale from templates.
- If a live foundation or architecture artifact is missing, initialize it from the matching `_template` file before applying user-provided or extracted content.
- Update the target live foundation or architecture artifact in place.
- Keep output durable, structured, concise, and usable by later work-item stages.

## Work-Item Target Pattern

- Use the current work item when clear; otherwise ask the user to select one, following the Interactive Question Pattern.
- Work-item folders must follow the [Work-Item Folder Naming Pattern](#work-item-folder-naming-pattern) when created by `/devspec.story`.
- Treat optional user input as additive guidance only.
- Update the target work-item artifact in place and stay within the current stage scope; after finalization, stay within the finalized scope.

## Work-Item Folder Naming Pattern

- New work-item folders must use `<provider-prefix-optional>-<story-number>-<kebab-case-title>`.
- Validate new folder names with `^(?:[A-Z]{3,5}-)?[0-9]+-[a-z0-9]+(?:-[a-z0-9]+)*$`.
- Provider prefix is optional. When present, it must be 3-5 uppercase letters. Use known mappings where available: GitHub -> `GHUB`, Azure DevOps -> `ADO`, Jira -> `JIRA`.
- Story number must be numeric and should come from the resolved provider item, issue number, work item id, or manually supplied external reference.
- Title slug must be lowercase kebab-case from the resolved provider title or manually supplied title. Remove punctuation, replace separators with hyphens, collapse repeated hyphens, and trim leading or trailing hyphens.
- If provider prefix, numeric story number, or title slug is missing or ambiguous, ask exactly one structured question before creating the folder.
- Do not create or rename a work-item folder until the generated folder name is valid or the user confirms a custom valid name.
- Do not automatically rename existing work-item folders. Treat non-matching existing folders as legacy and continue using them unless the user explicitly asks to rename.

## Multi-Repo Validation Pattern

- `devspec/foundation/codebase-structure.md` is the single source of truth for multi-repo configuration.
- Validate repo role, local path, current workspace availability, and access requirement there before planning or implementation depends on a repo.
- Treat repo location, workspace membership, and access requirement as separate facts. A repo outside the current repo folder or outside the current workspace must not be automatically classified as `reference-only`.
- Do not infer, default, or backfill missing access requirements. In particular, do not assume `reference-only`.
- For each repo with a missing or ambiguous access requirement, ask exactly one repo-specific multiple-choice confirmation before writing or relying on that repo configuration.
- Access requirement confirmation options must be limited to `reference-only`, `edit`, `edit-and-test`, `validation-only`, `release-coordination`, `blocked`, and `Custom Answer`.
- Respect access requirements: do not edit repos marked `reference-only`, `validation-only`, `release-coordination`, or `blocked` unless the user explicitly confirms a scope change.
- Do not run validation in repos marked `reference-only`, `release-coordination`, or `blocked` unless the user explicitly confirms a scope change.
- For multi-repo work, stop and surface a blocker instead of guessing when required repo configuration is missing, outdated, or inaccessible.
- For single-repo work, do not require multi-repo configuration.

## Explore and Memory Pattern

- Follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern) before repository discovery, code search, or Explore runs.
- Use `Explore` when repository discovery, analogous implementations, impacted areas, or likely blockers cannot be resolved cheaply from the current artifact context.
- Persist only transient working-state summaries to `/memories/session/<stage>.md`; do not treat session memory as the canonical source of truth.
- Keep session memory concise and structured with objective, findings, open questions, decisions, and next recommended step.
- Update session memory only after meaningful discovery or scope changes, not after every minor step.
- If clarification changes the scope or invalidates prior findings, rerun discovery as needed and replace stale memory sections instead of appending conflicting notes.
- Write final user-visible results and durable workflow state to the stage artifact, not only to session memory.
