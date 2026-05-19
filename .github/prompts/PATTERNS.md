# Shared Prompt Patterns

Use this file to keep repeated workflow behavior out of individual prompt and agent contracts.

## Interactive Question Pattern

- Ask exactly one blocking clarification, confirmation, or selection question at a time.
- Use clickable multiple-choice options whenever reasonable.
- Always include a `Custom Answer` option.
- Recommend exactly one option with a short justification.
- Wait for the user's answer before asking the next question.
- Do not bundle unrelated questions into one message.
- If multiple confirmations are discovered at once, present only the highest-priority one and defer the rest until after the user answers.

## Prerequisite Validation Pattern

- Validate required user input and required upstream artifacts before producing output.
- If a required prerequisite is missing, invalid, ambiguous, or not ready, stop immediately, explain the blocker, and direct the user to the correct recovery step.
- Record unresolved blockers only when the user declines to answer or the evidence remains unavailable.
- Treat optional user input as additive guidance only unless the stage explicitly requires user input.

## Output Closure Pattern

- End with a recommended next step or next prompt to run.
- Summarize only the artifact or work-item path updated, the key outcome, blockers or open questions, and the recommended next step.

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
- Treat optional user input as additive guidance only.
- Update the target work-item artifact in place and stay within the current stage scope; after finalization, stay within the finalized scope.

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
