# Devspec Prompt Index

Slash-command prompts live here. Keep behavior in `PATTERNS.md`, matching agents, or canonical devspec artifacts.

Artifacts should be developer-facing and compact. Prefer tables for stack, source evidence, repository configuration, boundaries, rules, tasks, readiness, and validation; use bullets for direct facts; use ordered lists only when sequence matters. Omit optional sections when they have no real content.

## Workflow

Foundation: `extract` -> `projectcontext` -> `techstack` -> `codebase-structure` -> `coding-standards` -> `rules`

Work items: `story` -> `finalize` -> `tasks` -> `implement` -> `review`

Use `clarify` only when work-item intake or finalization records a blocking question.

Supporting: `diagram`

`/devspec.extract` can be run with blank input to choose `Use current project root`, `Enter repo paths`, or `Cancel extraction`; it also accepts one repo URL or local path, or named multi-repo input such as `UI - D:\repo-ui, API - D:\repo-api`.

## Registered Slash Commands

The registered devspec slash commands are:

- `/devspec.extract`
- `/devspec.projectcontext`
- `/devspec.techstack`
- `/devspec.codebase-structure`
- `/devspec.coding-standards`
- `/devspec.rules`
- `/devspec.story`
- `/devspec.clarify`
- `/devspec.finalize`
- `/devspec.tasks`
- `/devspec.implement`
- `/devspec.review`
- `/devspec.diagram`

Recommendation behavior is defined by `PATTERNS.md#registered-command-recommendation-pattern`.

Developers invoke registered slash commands from this directory. Agent names are workflow targets and may be internal handoff details; do not recommend an agent name as a slash command unless the matching prompt is registered here.

## Shared References

- `PATTERNS.md`: shared workflow, recovery, output, discovery, foundation, work-item, memory, and multi-repo rules.
- `PATTERNS.md#artifact-content-pattern`: shared structure rules for developer-facing artifacts, source labels, optional sections, and table/bullet/list usage.
- `PATTERNS.md#diagram-extraction-consistency-pattern`: shared diagram candidate, evidence, confidence, dedupe, and diagram queue rules.
- `../../devspec/foundation/rules.md`: operational rules, work-item handling rules, exceptions, and delivery gates.
- `../../devspec/foundation/codebase-structure.md`: multi-repo source of truth.
- `../../devspec/foundation/discovery-exclusions.md`: baseline exclusions, ecosystem discovery rules, and project-specific overrides for repository discovery.
- `../../devspec/foundation/exploration-state.md`: optional method ledger for reusable working, failed, and superseded discovery methods; create only when there is reusable state to preserve.
- `../../devspec/foundation/provider-integrations.md`: manually maintained provider resolution, confirmation, integration access, and manual fallback policy.
- `../skills/exploration-recovery/SKILL.md`: reusable GitHub skill for avoiding repeated failed exploration paths.
- `../../devspec/foundation/_template/`: framework-owned section contracts for foundation artifacts.
- `../../devspec/architecture/_template/`: framework-owned section contracts for architecture artifacts.
- `../../devspec/architecture/_template/decision.md`: framework-owned ADR section contract; create `../../devspec/architecture/decisions/` only when an ADR is needed.
- `../../devspec/work-items/_template/`: durable work-item artifact shapes.

## Model Policy

See [Model recommendations](../../README.md#model-recommendations). Agent frontmatter owns model fallback order; VS Code model-picker settings own thinking effort.

## Prompt Map

| Prompt | Purpose | Produces |
| --- | --- | --- |
| `devspec.extract.prompt.md` | Derive structured, evidence-backed constitution candidates, architecture context, and live foundation facts from current root, repo URLs, local paths, or named multi-repo input. | `constitution.md`, `architecture/overview.md`, live `foundation/*.md` |
| `devspec.projectcontext.prompt.md` | Capture product purpose, audiences, stakeholders, outcomes, scope boundaries, metrics, delivery context, sources, confidence, and developer implications. | `foundation/project-context.md` |
| `devspec.techstack.prompt.md` | Capture technology stack inventory by project, support status, evidence, confidence, delivery constraints, and implementation impact. | `foundation/tech-stack.md` |
| `devspec.codebase-structure.prompt.md` | Capture selective repository trees, repository configuration, work areas and boundaries, integration contracts, and structure gaps or blockers. | `foundation/codebase-structure.md` |
| `devspec.coding-standards.prompt.md` | Capture an evidence-backed standards catalog with scoped rules, observed patterns, anti-patterns, source links, and optional short examples. | `foundation/coding-standards.md` |
| `devspec.rules.prompt.md` | Capture actionable operational rules, compliance requirements, forbidden patterns, delivery gates, work-item handling rules, exceptions, enforcement points, source, and confidence. | `foundation/rules.md` |
| `devspec.story.prompt.md` | Create or update work-item intake artifacts. | `meta.md`, `story.md`, `decisions.md`, `notes.md` |
| `devspec.clarify.prompt.md` | Ask, resolve, and record one active blocking clarification. | `clarify.md` |
| `devspec.finalize.prompt.md` | Create or update a structured implementation readiness brief with readiness assessment, implementation brief, validation plan, and blockers. | `finalize.md` |
| `devspec.tasks.prompt.md` | Break a ready brief into executable implementation tasks with planning basis, validation, and done criteria. | `tasks.md` |
| `devspec.implement.prompt.md` | Implement pending tasks and record implementation task ledger state, implementation evidence, execution history, and handoff details. | `implement.md`, code changes |
| `devspec.review.prompt.md` | Review implemented work against the finalized brief. | `review.md` |
| `devspec.diagram.prompt.md` | Generate or update one evidence-backed Mermaid diagram. | `architecture/diagrams/*.md` by default; `architecture/overview.md` for high-level architecture diagrams; work-item `diagrams.md` for explicit or temporary generated diagram content |

## Maintenance

- Keep prompts stage-specific and concise.
- Keep agents focused on execution, tools, and handoffs.
- Put shared mechanics in `PATTERNS.md`.
- Put operational gates in `../../devspec/foundation/rules.md`.
- Update the matching prompt, agent, and `_template` contract together when a stage contract changes.
