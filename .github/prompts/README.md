# Devspec Prompt Index

Slash-command prompts live here. Put reusable behavior in `PATTERNS.md`, matching agents, or canonical devspec artifacts.

Artifacts should be developer-facing and compact. Prefer tables for stack, source evidence, repository configuration, boundaries, rules, tasks, readiness, and validation; use bullets for direct facts; use ordered lists only when sequence matters. Omit optional sections when they have no real content.

## Workflow

Foundation: `extract` -> `projectcontext` -> `techstack` -> `codebase-structure` -> `coding-standards` -> `rules`

Work items: `story` -> `finalize` -> `tasks` -> `implement` -> `review`

Use `clarify` only when work-item intake or finalization records a blocking question.

Supporting: `diagram`

`/devspec.extract` can run with blank input to choose `Use current project root`, `Enter repo paths`, or `Cancel extraction`; it also accepts one repository URL or local path, or named multi-repo input such as `UI - D:\repo-ui, API - D:\repo-api`.

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

Developers invoke registered slash commands from this directory. Agent names are workflow targets used for internal handoffs; do not recommend an agent name as a slash command unless the matching prompt is registered here.

## Shared References

- `PATTERNS.md`: shared workflow, recovery, output, discovery, foundation, work-item, memory, and multi-repo rules.
- `../../devspec/adapters/command-registry.md`: provider-neutral registry for every registered `devspec` command, canonical prompt and agent source, output artifacts, mutation level, and handoff.
- `../../devspec/adapters/validation-flows.md`: enterprise acceptance checklists for new repository, existing repository, story lifecycle, and cross-tool recovery validation.
- `../../devspec/adapters/gemini-cli.md` and `../../devspec/adapters/antigravity.md`: Gemini CLI and Google Antigravity adapter guidance.
- `PATTERNS.md#artifact-content-pattern`: shared structure rules for developer-facing artifacts, source labels, optional sections, and table/bullet/list usage.
- `PATTERNS.md#task-quality-gate-pattern`: shared task planning, implementation, and review alignment rules for source refs, dependency order, granularity, blockers, validation evidence, and task-scope drift.
- `PATTERNS.md#constitution-amendment-pattern`: confirmation-gated durable principle changes, artifact routing, consistency review, and placeholder safety.
- `PATTERNS.md#diagram-extraction-consistency-pattern`: shared diagram candidate, naming, output format, Mermaid declaration, SVG target, evidence, confidence, dedupe, tags, and diagram queue rules.
- `PATTERNS.md#svg-output-pattern`: standalone SVG output rules, folders, template selection, validation, and forbidden elements.
- `PATTERNS.md#process-flow-extraction-pattern`: process-flow discovery, tagging, hybrid user-to-data operational flow, and batch-generation rules.
- `../../devspec/constitution.md`: rare durable principles across work items and agents; principle-level changes require confirmation and consistency review.
- `../../devspec/foundation/project-context.md`: product purpose, audiences, outcomes, scope, metrics, and product delivery context.
- `../../devspec/foundation/rules.md`: operational rules, compliance requirements, governance procedures, work-item handling rules, exceptions, and delivery gates.
- `../../devspec/foundation/codebase-structure.md`: multi-repo source of truth.
- `../../devspec/foundation/discovery-exclusions.md`: baseline exclusions, ecosystem discovery rules, and project-specific overrides for repository discovery.
- `../../devspec/foundation/extraction-state.md`: extraction queue, resume state, blockers, and confirmations for `/devspec.extract`.
- `../../devspec/foundation/exploration-state.md`: optional method ledger for reusable working, failed, and superseded discovery methods; create only when there is reusable state to preserve.
- `../../devspec/foundation/provider-integrations.md`: manually maintained provider lookup, confirmation, integration access, and manual fallback policy.
- `../skills/exploration-recovery/SKILL.md`: reusable skill for avoiding repeated failed exploration paths.
- `../../devspec/foundation/_template/`: framework-owned section contracts for foundation artifacts.
- `../../devspec/architecture/_template/`: framework-owned section contracts for architecture artifacts.
- `../../devspec/architecture/_template/decision.md`: framework-owned ADR section contract; create `../../devspec/architecture/decisions/` only when an ADR is needed.
- `../../devspec/work-items/_template/`: durable work-item artifact shapes.

## Model Policy

See [Model recommendations](../../README.md#model-recommendations). Agent front matter owns model fallback order; VS Code model picker settings own thinking effort.

## Prompt Map

| Prompt | Purpose | Produces |
| --- | --- | --- |
| `devspec.extract.prompt.md` | Derive structured, evidence-backed constitution candidates, architecture context, live foundation facts, process-flow queue candidates, and language-neutral diagram queue candidates from current root, repository URLs, local paths, or named multi-repo input; constitution candidates remain confirmation-gated. | `foundation/extraction-state.md`, `constitution.md`, `architecture/overview.md`, `architecture/artifact-queue.md`, live `foundation/*.md` |
| `devspec.projectcontext.prompt.md` | Capture product purpose, audiences, stakeholders, outcomes, scope boundaries, metrics, delivery context, sources, confidence, and developer implications; route principles and operational governance to their own artifacts. | `foundation/project-context.md` |
| `devspec.techstack.prompt.md` | Capture technology stack inventory by project, support status, evidence, confidence, delivery constraints, and implementation impact. | `foundation/tech-stack.md` |
| `devspec.codebase-structure.prompt.md` | Capture selective repository trees, repository configuration, work areas and boundaries, integration contracts, and structure gaps or blockers. | `foundation/codebase-structure.md` |
| `devspec.coding-standards.prompt.md` | Capture an evidence-backed standards catalog with scoped rules, observed patterns, anti-patterns, source links, and optional short examples. | `foundation/coding-standards.md` |
| `devspec.rules.prompt.md` | Capture actionable operational rules, compliance requirements, forbidden patterns, delivery gates, work-item handling rules, exceptions, enforcement points, source, and confidence. | `foundation/rules.md` |
| `devspec.story.prompt.md` | Create or update one work-item intake. | `meta.md`, `story.md`, `decisions.md`, `notes.md` |
| `devspec.clarify.prompt.md` | Ask, resolve, and record one active blocking clarification. | `clarify.md` |
| `devspec.finalize.prompt.md` | Create or update a structured implementation readiness brief with readiness assessment, foundation and architecture alignment, implementation brief, validation plan, and blockers. | `finalize.md` |
| `devspec.tasks.prompt.md` | Break a ready brief into source-referenced executable implementation tasks with task-quality review, validation, and done criteria. | `tasks.md` |
| `devspec.implement.prompt.md` | Implement pending tasks and record task-quality checks, task-row progress, implementation evidence, execution history, and handoff details. | `implement.md`, `tasks.md` status updates, code changes |
| `devspec.review.prompt.md` | Review implemented work against the finalized brief, tasks, and implementation record. | `review.md` |
| `devspec.diagram.prompt.md` | Generate or update one evidence-backed diagram, defaulting to Mermaid with opt-in SVG output, or batch-generate queued process-flow diagrams. | `architecture/diagrams/dia-NNN-*.md` by default; optional `architecture/images/dia-NNN-*.svg` for `format=svg` or `format=mermaid+svg`; `architecture/overview.md` for high-level architecture diagrams; work-item `diagrams.md` and optional `images/*.svg` for explicit or clearly temporary work-item-specific diagram content |

## Maintenance

- Keep prompts stage-specific and concise.
- Keep agents focused on execution, tools, and handoffs.
- Keep adapter support additive; do not change prompt or agent intent to satisfy another tool.
- Update `../../devspec/adapters/command-registry.md` whenever a registered command contract changes.
- Put shared mechanics in `PATTERNS.md`.
- Put durable principles in `../../devspec/constitution.md` only after explicit confirmation and consistency review.
- Put operational gates in `../../devspec/foundation/rules.md`.
- Update the matching prompt, agent, and `_template` contract together when a stage contract changes.
