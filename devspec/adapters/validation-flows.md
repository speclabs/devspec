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
| 1 | `/devspec.story` | `meta.md`, `story.md`, `decisions.md`, and `notes.md` exist under one valid work-item folder. |
| 2 | `/devspec.clarify` when blocked | `clarify.md` records the active question, answer, resolution, and remaining blockers. |
| 3 | `/devspec.finalize` | `finalize.md` records readiness, foundation and architecture alignment, implementation brief, validation plan, assumptions, and blockers. |
| 4 | `/devspec.tasks` | `tasks.md` records executable tasks with repository, target area, validation, done criteria, dependencies, and status. |
| 5 | `/devspec.implement` | `implement.md` records repository access checks, task ledger, attempts, changed files or areas, validation results, blockers, and resume state. |
| 6 | `/devspec.review` | `review.md` records findings, scope adherence, validation gaps, rule violations, and review status. |

Acceptance checklist:

- Work-item state uses values from `devspec/glossary.md`.
- `finalize.md` must be `ready` before `/devspec.tasks` plans implementation tasks.
- `/devspec.finalize` records or blocks on applicable constitution, foundation, architecture, delivery-gate, repository-readiness, and validation-traceability gaps before marking `ready`.
- `/devspec.tasks` does not expand scope beyond the finalized brief.
- `/devspec.implement` respects repository access requirements from `devspec/foundation/codebase-structure.md`.
- `/devspec.review` reviews against the finalized brief instead of re-planning.

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
