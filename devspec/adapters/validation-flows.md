# Enterprise Validation Flows

Use these flows as release gates for multi-agent support. Run them per adapter before declaring the adapter enterprise-ready.

## New Repository Flow

Validate the foundation path for a repository with little or no implementation code.

| Step | Command | Expected evidence |
| --- | --- | --- |
| 1 | `/devspec.projectcontext` | `devspec/foundation/project-context.md` captures product purpose, users, outcomes, scope boundaries, sources, confidence, and developer implications. |
| 2 | `/devspec.techstack` | `devspec/foundation/tech-stack.md` captures stack choices, support status, hosting or tooling constraints, sources, and confidence. |
| 3 | `/devspec.codebase-structure` | `devspec/foundation/codebase-structure.md` captures planned or existing layout, work areas, integration boundaries, and repository access expectations. |
| 4 | `/devspec.coding-standards` | `devspec/foundation/coding-standards.md` captures implementation standards, testing expectations, observed or selected patterns, and blockers. |
| 5 | `/devspec.rules` | `devspec/foundation/rules.md` captures operational rules, compliance requirements, delivery gates, and work-item handling rules. |

Acceptance checklist:

- No extraction step is required.
- Every generated artifact uses its live foundation file, not the `_template` file as the final output.
- Every command records blockers or confidence gaps instead of guessing.
- Durable principle changes require explicit confirmation and a consistency review against project context, operational rules, prompts, agents, templates, adapter guidance, and validation docs.
- The next recommended action follows `devspec/adapters/command-registry.md`.

## Existing Repository Flow

Validate the foundation path for a repository or multi-repo system that already contains implementation evidence.

| Step | Command | Expected evidence |
| --- | --- | --- |
| 1 | `/devspec.extract` | `devspec/foundation/extraction-state.md`, `devspec/architecture/overview.md`, `devspec/architecture/artifact-queue.md`, and live foundation artifacts are seeded from evidence. |
| 2 | `/devspec.projectcontext` | Product context is refined with human business context that code cannot fully prove. |
| 3 | `/devspec.techstack` | Extracted stack evidence is confirmed or corrected. |
| 4 | `/devspec.codebase-structure` | Repository layout, work areas, multi-repo access, and boundaries are confirmed. |
| 5 | `/devspec.coding-standards` | Evidence-backed coding standards and anti-patterns are confirmed. |
| 6 | `/devspec.rules` | Operational and compliance rules are confirmed or added. |

Acceptance checklist:

- Discovery exclusions from `devspec/foundation/discovery-exclusions.md` are respected.
- Extraction does not rewrite `devspec/constitution.md` principles from code inference without confirmation and constitution amendment consistency review.
- Missing evidence, access issues, and unresolved provider lookup paths are recorded as blockers.
- Extracted facts are placed in their target artifacts, not left only in extraction notes.

## End-To-End Story Flow

Validate one full feature, bug, or security-vulnerability lifecycle after the foundation exists.

| Step | Command | Expected evidence |
| --- | --- | --- |
| 1 | `/devspec.story` | `meta.md`, `story.md`, `decisions.md`, and `notes.md` exist under one valid work-item folder; `story.md` records one-story scope, readable intake sections, and observable acceptance criteria or a recorded blocker. |
| 2 | `/devspec.clarify` when blocked | `clarify.md` records the active question, answer, resolution, and remaining blockers. |
| 3 | `/devspec.finalize` | `finalize.md` records readiness, foundation and architecture alignment, implementation brief, validation plan, assumptions, and blockers. |
| 4 | `/devspec.tasks` | `tasks.md` records task-quality review, scope, source refs, executable tasks with repository, target area, validation, done criteria, dependencies, and status. |
| 5 | `/devspec.implement` | `implement.md` records repository access checks, task quality checks, task ledger, attempts, changed files or areas, validation results, blockers, and resume state; `tasks.md` task-row progress fields stay aligned. |
| 6 | `/devspec.review` | `review.md` records findings, scope adherence, task completion alignment, source-ref alignment, validation gaps, rule violations, and review status. |

Acceptance checklist:

- Work-item state uses values from `devspec/glossary.md`.
- `/devspec.story` handles one independent story, feature, bug, security issue, task, or PBI per work-item folder.
- `story.md` keeps source tracking, summary, description, acceptance criteria, functional requirements, nonfunctional requirements, edge cases, and planning signals in distinct sections without duplicating routing details from `meta.md`.
- Acceptance criteria captured during intake are specific and testable, or the missing criteria are recorded as a blocker.
- `finalize.md` must be `ready` before `/devspec.tasks` plans implementation tasks.
- `/devspec.finalize` records or blocks on applicable constitution, foundation, architecture, delivery-gate, repository-readiness, and validation-traceability gaps before marking `ready`.
- `/devspec.tasks` does not expand scope beyond the finalized brief and records task-quality checks before implementation handoff.
- `/devspec.tasks` includes scope and source refs from finalized acceptance criteria, implementation brief rows, validation plan rows, risks, or follow-ups for every executable task.
- `/devspec.implement` respects repository access requirements from `devspec/foundation/codebase-structure.md`.
- `/devspec.implement` keeps `tasks.md` task-row status, attempt count, and checkpoint fields aligned with `implement.md`.
- `/devspec.implement` records blockers, ambiguity, skipped tasks, oversized task scope, and validation outcomes without silently expanding task scope.
- `/devspec.review` reviews against the finalized brief, tasks, implementation record, and changed work instead of re-planning.
- `/devspec.review` flags missing task coverage, skipped or blocked tasks without rationale, missing validation evidence, source-ref drift, and implementation beyond task scope when they affect close readiness.

## Append-Only Change Request Scenario

Validate that post-baseline scope changes preserve the original story ledger.

| Step | Command | Expected evidence |
| --- | --- | --- |
| 1 | `/devspec.story` with `.NET 10 upgrade` | Baseline `story.md` records the upgrade scope with `AC-*`, `FR-*`, and related planning rows. |
| 2 | `/devspec.finalize` -> `/devspec.tasks` -> `/devspec.implement` | Baseline `finalize.md`, `tasks.md`, and `implement.md` record ready scope, `baseline` task rows such as `T-001..T-003`, and implementation evidence. |
| 3 | `/devspec.story` with `Change request for existing .NET 10 upgrade story: increase code coverage from 60% to 80%` | `story.md#change-requests` appends `CR-001`; CR-scoped criteria such as `CR-001-AC-001` are added without rewriting baseline summary, description, or criteria. |
| 4 | `/devspec.finalize` -> `/devspec.tasks` -> `/devspec.implement` | `finalize.md` appends `CR-001` readiness, implementation brief, and validation rows; `tasks.md` appends new `Scope` = `CR-001` rows after the highest existing task ID; `implement.md` appends CR-scoped evidence and execution-log rows while `tasks.md` updates only the matching `CR-001` task rows. |
| 5 | `/devspec.story` with another related request | `story.md#change-requests` appends `CR-002`; task planning later appends new task IDs without renumbering or rewriting `CR-001` or baseline rows. |
| 6 | `/devspec.story` with an unrelated feature request for the same target | The agent asks one structured `selection` question to append to the current item, create a new linked work item, or provide `Custom Answer`; when the linked-item option is chosen, the new work-item folder follows the standard folder naming pattern, its `meta.md#work-item-record` `Parent work item` points to the original item, and the original item does not receive a `CR-###` row for that linked request. |
| 7 | `/devspec.clarify` with post-baseline scope input | `clarify.md` records routing to `/devspec.story`; baseline intake remains unchanged. |
| 8 | `/devspec.review` | Review flags missing CR task rows, missing CR source refs, CR work implemented outside appended tasks, source-ref drift, or overwritten baseline content. |

Acceptance checklist:

- `story.md#change-requests` uses disposition values from `devspec/glossary.md#change-request-disposition-values`.
- Related post-baseline changes append `CR-###` rows inside the existing work-item folder.
- Independent or unrelated changes trigger a structured selection before writing.
- Choosing a linked work item creates or updates a separate work-item folder that follows `devspec` folder naming rules and records the original item in `meta.md#work-item-record` `Parent work item`.
- Linked work-item routing does not add a `CR-###` row to the original work item's `story.md#change-requests`.
- Baseline `AC-*`, task rows, implementation evidence, and review evidence remain intact.
- `tasks.md#implementation-tasks` includes `Scope` with `baseline` or `CR-###`.
- New CR task rows append after the highest existing `T-###`.
- `/devspec.implement` processes the active `CR-###` scope without rewriting baseline or prior CR implementation evidence.
- No `/devspec.change` command is introduced or recommended.

## Cross-Tool Recovery Scenario

Use this scenario to prove the framework is tool-neutral.

1. Start the new repository flow, existing repository flow, or story flow in one supported adapter.
2. Stop after a command writes a `Resume State` or workflow checkpoint.
3. Open the same repository in another supported adapter.
4. Ask the adapter to continue the same registered command or next handoff.
5. Confirm it reads Git-tracked `devspec` artifacts first and continues from the recorded checkpoint.

Acceptance checklist:

- The second adapter does not rely on the first adapter's chat history.
- The second adapter preserves pending questions, blockers, current task, and next action.
- Any unsupported platform feature is recorded as a limitation, not converted into a workflow change.

## Adapter Wrapper Checks

Run these checks before enterprise release:

| Adapter | Required wrapper evidence |
| --- | --- |
| Gemini CLI | Root `GEMINI.md` exists; `.gemini/commands/devspec/*.toml` has one wrapper for each registered command; native command names map `/devspec.story` to `/devspec:story` style names. |
| Google Antigravity | `.agents/rules/devspec-workflow.md` exists; `.agents/skills/devspec-*.md` has one wrapper for each registered command; native skill names map `/devspec.story` to `/devspec-story` style names. |

Each wrapper must reference `devspec/adapters/command-registry.md` and the matching canonical Copilot prompt and agent files.
