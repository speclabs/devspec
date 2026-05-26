# Devspec Prompt Index

Slash-command prompts live here. Keep behavior in `PATTERNS.md`, matching agents, or canonical devspec artifacts.

Artifacts should be developer-facing and compact. Prefer tables for stack, source evidence, repo configuration, boundaries, rules, tasks, readiness, and validation; use bullets for direct facts; use ordered lists only when sequence matters. Omit optional sections when they have no real content.

## Workflow

Foundation: `extract` -> `projectcontext` -> `techstack` -> `codebase-structure` -> `coding-standards` -> `rules`

Work items: `story` -> `finalize` -> `tasks` -> `implement` -> `review`

Use `clarify` only when story intake or finalization records a blocking question.

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
- `PATTERNS.md#diagram-extraction-consistency-pattern`: shared diagram candidate, evidence, confidence, dedupe, and queue rules.
- `../../devspec/foundation/rules.md`: bug, security, review, and delivery gates.
- `../../devspec/foundation/codebase-structure.md`: multi-repo source of truth.
- `../../devspec/foundation/discovery-exclusions.md`: default and project-specific paths to exclude from repository discovery.
- `../../devspec/foundation/exploration-state.md`: durable record of known working and failed discovery methods.
- `../../devspec/foundation/provider-integrations.md`: manually maintained provider intake and manual fallback policy.
- `../skills/exploration-recovery/SKILL.md`: reusable GitHub skill for avoiding repeated failed exploration paths.
- `../../devspec/foundation/_template/`: framework-owned section contracts for foundation artifacts.
- `../../devspec/architecture/_template/`: framework-owned section contracts for architecture artifacts.
- `../../devspec/architecture/decisions/_template.md`: framework-owned ADR section contract.
- `../../devspec/work-items/_template/`: durable work-item artifact shapes.

## Model Policy

See [Model recommendations](../../README.md#model-recommendations). Agent frontmatter owns model fallback order; VS Code model-picker settings own thinking effort.

## Prompt Map

| Prompt | Purpose | Produces |
| --- | --- | --- |
| `devspec.extract.prompt.md` | Derive structured, evidence-backed constitution candidates, architecture context, and live foundation facts from current root, repo URLs, local paths, or named multi-repo input. | `constitution.md`, `architecture/overview.md`, live `foundation/*.md` |
| `devspec.projectcontext.prompt.md` | Capture product vision, users, goals, non-goals, constraints, metrics, sources, confidence, and developer implications. | `foundation/project-context.md` |
| `devspec.techstack.prompt.md` | Capture languages, frameworks, services, tooling, hosting, versions, support status, evidence, and implementation guidance. | `foundation/tech-stack.md` |
| `devspec.codebase-structure.prompt.md` | Capture selective repo trees, module boundaries, ownership seams, integration contracts, multi-repo config, and placement rules. | `foundation/codebase-structure.md` |
| `devspec.coding-standards.prompt.md` | Capture an evidence-backed language/framework pattern catalog, source links, anti-patterns, and optional short examples. | `foundation/coding-standards.md` |
| `devspec.rules.prompt.md` | Capture actionable operational constraints, compliance, forbidden patterns, gates, enforcement points, source, and confidence. | `foundation/rules.md` |
| `devspec.story.prompt.md` | Create or update work-item intake artifacts. | `meta.md`, `story.md`, `decisions.md`, `notes.md` |
| `devspec.clarify.prompt.md` | Ask and record one blocking clarification. | `clarify.md` |
| `devspec.finalize.prompt.md` | Freeze a structured implementation-ready brief with readiness, scope, task planning inputs, validation plan, risks, and blockers. | `finalize.md` |
| `devspec.tasks.prompt.md` | Break a ready brief into executable ordered tasks with target areas, dependencies, validation, and done criteria. | `tasks.md` |
| `devspec.implement.prompt.md` | Implement pending tasks and record compact recovery checkpoints, changed files, validation, and handoff details. | `implement.md`, code changes |
| `devspec.review.prompt.md` | Review implemented work against the finalized brief. | `review.md` |
| `devspec.diagram.prompt.md` | Generate or update one evidence-backed Mermaid diagram. | `architecture/diagrams/*.md` by default; `architecture/overview.md` for high-level system diagrams; work-item `diagrams.md` for explicit or temporary work-item diagrams |

## Maintenance

- Keep prompts stage-specific and concise.
- Keep agents focused on execution, tools, and handoffs.
- Put shared mechanics in `PATTERNS.md`.
- Put operational gates in `../../devspec/foundation/rules.md`.
- Update the matching prompt, agent, and `_template` contract together when a stage contract changes.
