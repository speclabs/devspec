# Shared Prompt Patterns

Keep repeated workflow behavior here instead of duplicating it in every prompt or agent.

## Interactive Question Pattern

- Ask exactly one blocking clarification, confirmation, or selection question at a time.
- Use clickable multiple-choice options whenever reasonable; explicit options are required for confirmations and workflow decisions.
- Always include a `Custom Answer` option.
- Recommend exactly one option with a short justification.
- Use `Yes`, `No`, and `Custom Answer` for binary confirmations.
- Use `Proceed`, `Skip`, and `Custom Answer` for workflow continuation, queue processing, task continuation, generated artifact approval, or retry decisions.
- Use `Continue`, `Pause`, `Skip`, and `Custom Answer` when resuming a run from `stopped` or ambiguous state.
- Use domain-specific option sets only when the stage defines them, such as provider intake actions or multi-repo access requirement values.
- Wait for the user's answer before asking another question.
- If several confirmations are discovered, present only the highest-priority one and defer the rest.

## Next Action Selection Pattern

- Recommend one next step.
- Do not output multiple next prompts, command lists, or peer next-action bullets while a clarification, confirmation, queue item, handoff, retry, or fallback decision is pending.
- When several next actions are possible, pick the highest-priority unresolved action and ask one structured question using the [Interactive Question Pattern](#interactive-question-pattern).
- If no confirmation or selection is pending, provide exactly one registered slash command, handoff, file update, or structured question.
- For queues, select the next unresolved item by queue order and status unless the stage defines stricter priority.
- A final response may summarize completed work, but it must close with one next action or one structured question.

## Registered Command Recommendation Pattern

- Use `.github/prompts/README.md#registered-slash-commands` as the command registry.
- Recommend only registered slash commands; do not invent commands from workflow names, artifact names, queue names, or agent names.
- Do not recommend unregistered commands such as `/devspec.plan`, `/devspec.architecture`, `/devspec.provider-integrations`, `/devspec.queue`, or `/devspec.decisions`.
- Before recommending a slash command, verify it is registered and the matching `.github/prompts/devspec.<command>.prompt.md` file exists.
- If no registered command fits, recommend a concrete file update, configured handoff, or structured question.
- Map common workflow labels to registered commands when appropriate: planning -> `/devspec.tasks`, implementation -> `/devspec.implement`, review -> `/devspec.review`, diagram generation -> `/devspec.diagram`, and provider integration changes -> manual updates in `devspec/foundation/provider-integrations.md`.

## Prerequisite Validation Pattern

- Validate required user input and upstream artifacts before producing output.
- If a prerequisite is missing, invalid, ambiguous, or not ready, stop, explain the blocker, and direct the user to the recovery step.
- Record unresolved blockers only when the user declines to answer or evidence remains unavailable.
- Treat optional user input as additive guidance unless the stage explicitly requires it.

## Session Recovery Pattern

- Treat Git-tracked `devspec` artifacts as canonical; chat history and session memory are supporting context only.
- At the start of each applicable command, read the target artifact and durable state files, then reconcile `Resume State`.
- Use work-item folders as the orchestration boundary. Use tasks, target repos, target areas, and attempts as checkpoints.
- For monorepos, record the target repo once and distinguish tasks by module, layer, or area. For multi-repo work, every executable task must name target repo and required access.
- Keep `Run status` values limited to `active`, `waiting-for-user`, `paused`, `stopped`, `blocked`, and `complete`.
- Use `paused` when the user expects to continue from the same task or question.
- Use `stopped` when the run intentionally ended and should ask one continuation question before resuming.
- Use `blocked` only when evidence, access, or prerequisites are insufficient; record the blocker and continuation condition.
- Before any blocking question, handoff, retry-loop stop, or run end, update `Resume State` with stage, item, last completed step, pending question, recommended option, resume command, and next required action.
- On rerun, resume a `paused` item directly when prerequisites still hold; for `stopped` or ambiguous state, ask one structured continuation question first.
- Retry only when the recorded retry condition is met, the user gives custom direction, or the method materially changed. Do not replay known failed methods just because the session changed.
- When stage tasks or queue items are complete, mark the stage `complete` and hand off to the next registered command or configured agent.

## Output Closure Pattern

- Follow the [Next Action Selection Pattern](#next-action-selection-pattern).
- Follow the [Registered Command Recommendation Pattern](#registered-command-recommendation-pattern) before recommending any slash command.
- End with exactly one registered command, handoff, file update, or structured question.
- If the next step requires confirmation, selection, retry approval, queue approval, or continuation, ask one structured question with explicit options.
- Summarize only the artifact or work-item path updated, key outcome, blockers or open questions, and single next action.

## Token Stewardship Pattern

- Prefer canonical references over restating policy, templates, or provider rules.
- Keep stage artifacts concise: record decisions, evidence, blockers, validation, and handoffs; omit narrative filler.
- Do not duplicate content already captured in another devspec artifact. Link or name the source instead.
- Preserve user-authored content with targeted edits instead of whole-file rewrites.

## Artifact Content Pattern

- Write artifacts for developers who need to plan, implement, review, or recover work. Every captured item should make clear what is true, where it applies, what evidence or source supports it, and what a developer should do with it.
- Prefer Markdown tables for matrix data, including stack details, source evidence, repo configuration, module boundaries, rules, readiness, tasks, validations, and comparison-style decisions.
- Prefer bullets for direct facts, rules, assumptions, blockers, and concise developer guidance.
- Prefer ordered lists only for workflows, procedures, reproduction steps, migration steps, or task sequences where order changes the result.
- Avoid theory, generic explanations, restated prompt policy, and broad background that does not change a developer's next action.
- Do not keep optional sections only to satisfy a template. Omit sections, tables, or rows that have no real project content, unless the empty section is required for resume state or a command contract.
- Use source labels consistently: `confirmed` for user-provided or approved facts, `observed` for direct repository evidence, `inferred` for reasoned conclusions from evidence, and `blocked` for unresolved gaps.
- Preserve useful existing content, but replace stale, vague, or duplicative prose with compact structured records.

## Discovery Exclusion Pattern

- Before repository search, extraction, code-pattern discovery, layout mapping, validation-surface discovery, or generated helper scripts, read `devspec/foundation/discovery-exclusions.md` when present.
- Exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output folders by default. Do not infer project conventions from installed dependency or generated output source.
- Use manifests, lockfiles, and framework config files for dependencies and tooling; inspect dependency folders only when the user asks or a project override permits it.
- Respect repository ignore files as a baseline, while still applying this pattern.
- Apply ecosystem and framework exclusions from `devspec/foundation/discovery-exclusions.md`; initialize it from `devspec/foundation/_template/discovery-exclusions.md` when missing.
- Keep source discovery focused on owned source roots, tests, scripts, config, infrastructure, docs, manifests, and routing-critical files.
- Record project-specific include or exclude exceptions in `devspec/foundation/discovery-exclusions.md`, not individual stage artifacts.

## Diagram Extraction Consistency Pattern

- Use this pattern when extraction proposes diagram candidates or `/devspec.diagram` generates or updates a diagram.
- Queue only candidates backed by concrete repository evidence from owned routes, modules, workflows, state transitions, services, integrations, ADRs, docs, infrastructure, runtime config, or manifests.
- Each queued candidate must include ID, scope, Mermaid type, subject, target path, evidence source, confidence, status, output section, notes, and the result of an equivalent-diagram check.
- Use stable IDs such as `DIA-001`, `DIA-002`, preserving existing IDs and assigning the next available number for new rows.
- Keep subjects specific enough to become one diagram file. Use lowercase kebab-case for subject slugs, one subject per diagram file, and `devspec/architecture/diagrams/<subject-slug>.md` for durable diagrams.
- Prefer reusable architecture, module, feature, workflow, sequence, state, or user-journey diagrams over temporary work-item diagrams. Use work-item `diagrams.md` only for explicit or clearly temporary generated diagram content; keep diagram lifecycle status in `devspec/architecture/artifact-queue.md`.
- Use `flowchart` for module, feature, process, or data flow; `sequenceDiagram` for actor or service interactions over time; `journey` for user-facing paths; `stateDiagram` for lifecycle or status transitions; and `classDiagram` for stable domain or structural relationships.
- Use confidence values consistently: `observed` for directly supported code, docs, config, or ADR evidence; `high-confidence` for inference from multiple local evidence points; `low-confidence` only when useful but incomplete evidence must be recorded as an assumption.
- Do not queue vague subjects, candidates without source evidence, duplicate or equivalent existing diagrams, or temporary work-item diagrams without an explicit request.
- Use `blocked` when a diagram idea is useful but evidence is insufficient; use `skipped` only after the user declines generation.
- Before queueing or writing, check `devspec/architecture/artifact-queue.md`, `devspec/architecture/overview.md`, `devspec/architecture/diagrams/*.md`, and relevant work-item `diagrams.md` files for equivalent subject, scope, type, or target path.
- Avoid duplicate overview diagrams unless `devspec/architecture/overview.md` lacks a confirmed high-level system view.
- During `/devspec.extract`, seed candidates in `devspec/architecture/artifact-queue.md` and ask about only the next unresolved candidate after higher-priority confirmations. Generate diagrams later through `/devspec.diagram` unless the user explicitly continues through the confirmed queue.
- During `/devspec.diagram`, reuse matching queue metadata instead of reclassifying the same subject from scratch, then generate exactly one evidence-backed Mermaid artifact per run.

## Exploration Recovery Pattern

- When `.github/skills/exploration-recovery/SKILL.md` is available, use it as the operational procedure.
- Before broad search, generated scripts, helper commands, provider lookup, or repeated discovery, follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern), then check `devspec/foundation/exploration-state.md` and session memory for known working and failed methods in the same scope.
- Use known working methods first when scope and goal match.
- Skip known failed methods unless input, environment, credentials, dependencies, access, path, or command changed.
- Prefer built-in repository search, targeted reads, manifest inspection, and configured provider tools before generating broad helper scripts.
- Limit probing to one new generated script, helper command, provider lookup path, or expensive search strategy per source or goal before falling back to direct search/read evidence gathering.
- When a fallback succeeds after a failed method, record scope, goal, failed method, reason, working method, and retry condition in `devspec/foundation/exploration-state.md`; optionally mirror a concise transient summary in `/memories/session/<stage>.md`.
- On rerun, use the recorded working method first and mention skipped known failures in the output.

## Foundation Update Pattern

- Required user input is mandatory.
- Ask one clarification at a time when required details are missing or ambiguous, following the Interactive Question Pattern.
- Follow the [Artifact Content Pattern](#artifact-content-pattern).
- Use the matching `devspec/foundation/_template/*.md` or `devspec/architecture/_template/*.md` file as the section contract when one exists.
- Treat live `devspec/foundation/*.md` and `devspec/architecture/*.md` files as project-owned; update them in place and never replace them wholesale from templates.
- If a live foundation or architecture artifact is missing, initialize it from the matching `_template` file before applying user-provided or extracted content.
- Keep output durable, structured, concise, and useful to later work-item stages.

## Work-Item Target Pattern

- Use the current work item when clear; otherwise ask the user to select one, following the Interactive Question Pattern.
- Work-item folders must follow the [Work-Item Folder Naming Pattern](#work-item-folder-naming-pattern) when created by `/devspec.story`.
- Follow the [Artifact Content Pattern](#artifact-content-pattern) when updating work-item artifacts.
- Treat optional user input as additive guidance only.
- Update the target work-item artifact in place. Stay within current stage scope and, after finalization, within finalized scope.

## Work-Item Folder Naming Pattern

- New work-item folders must use `<provider-prefix-optional>-<story-number>-<kebab-case-title>`.
- Validate new folder names with `^(?:[A-Z]{3,5}-)?[0-9]+-[a-z0-9]+(?:-[a-z0-9]+)*$`.
- Provider prefix is optional. When present, it must be 3-5 uppercase letters. Use known mappings where available: GitHub -> `GHUB`, Azure DevOps -> `ADO`, Jira -> `JIRA`.
- Story number must be numeric and should come from the resolved provider item, issue number, work item id, or manually supplied external reference.
- Title slug must be lowercase kebab-case from the resolved provider title or manually supplied title.
- Remove punctuation, replace separators with hyphens, collapse repeated hyphens, and trim leading or trailing hyphens.
- If provider prefix, numeric story number, or title slug is missing or ambiguous, ask exactly one structured question before creating the folder.
- Do not create or rename a work-item folder until the generated folder name is valid or the user confirms a custom valid name.
- Do not automatically rename existing work-item folders; treat non-matching existing folders as legacy and continue using them unless the user explicitly asks to rename.

## Multi-Repo Validation Pattern

- `devspec/foundation/codebase-structure.md` is the source of truth for multi-repo configuration.
- Validate repo role, local path, current workspace availability, and access requirement there before planning or implementation depends on a repo.
- Treat repo location, workspace membership, and access requirement as separate facts; do not classify a repo outside the current repo folder or workspace as `reference-only` based on location.
- Do not infer, default, or backfill missing access requirements. In particular, do not assume `reference-only`.
- For each repo with a missing or ambiguous access requirement, ask exactly one repo-specific multiple-choice confirmation before writing or relying on that configuration.
- Access requirement confirmation options must be limited to `reference-only`, `edit`, `edit-and-test`, `validation-only`, `release-coordination`, `blocked`, and `Custom Answer`.
- Respect access requirements: do not edit repos marked `reference-only`, `validation-only`, `release-coordination`, or `blocked` unless the user explicitly confirms a scope change.
- Do not run validation in repos marked `reference-only`, `release-coordination`, or `blocked` unless the user explicitly confirms a scope change.
- For multi-repo work, stop and surface a blocker instead of guessing when required repo configuration is missing, outdated, or inaccessible.
- For single-repo work, do not require multi-repo configuration.

## Explore and Memory Pattern

- Follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern) before repository discovery, code search, or Explore runs.
- Use `Explore` when repository discovery, analogous implementations, impacted areas, or likely blockers cannot be resolved cheaply from current artifact context.
- Persist only transient working-state summaries to `/memories/session/<stage>.md`; do not treat session memory as canonical.
- Keep session memory concise and structured with objective, findings, open questions, decisions, and next recommended step.
- Update session memory only after meaningful discovery or scope changes, not after every minor step.
- If clarification changes scope or invalidates findings, rerun discovery as needed and replace stale memory sections instead of appending conflicts.
- Write final user-visible results and durable workflow state to the stage artifact, not only to session memory.
