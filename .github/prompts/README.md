# Devspec Prompt Index

Slash-command prompts live here. Use this file as an index only; behavior belongs in `PATTERNS.md`, matching agents, or canonical devspec artifacts.

## Workflow

Foundation: `extract` -> `projectcontext` -> `techstack` -> `codebase-structure` -> `coding-standards` -> `rules`

Work items: `story` -> `clarify` -> `finalize` -> `tasks` -> `implement` -> `review`

## Shared References

- `PATTERNS.md`: shared interaction, prerequisite, token, output, foundation, work-item, memory, and multi-repo rules.
- `../../devspec/foundation/rules.md`: bug, security, review, and delivery gates.
- `../../devspec/foundation/codebase-structure.md`: multi-repo source of truth.
- `../../devspec/foundation/provider-integrations.md`: manually maintained provider intake and manual fallback policy.
- `../../devspec/foundation/_template/`: framework-owned section contracts for foundation artifacts.
- `../../devspec/architecture/_template/`: framework-owned section contracts for architecture artifacts.
- `../../devspec/architecture/decisions/_template.md`: framework-owned ADR section contract.
- `../../devspec/work-items/_template/`: durable work-item artifact shapes.

## Prompt Map

| Prompt | Purpose | Produces |
| --- | --- | --- |
| `devspec.extract.prompt.md` | Derive constitution candidates, architecture context, and live foundation facts from repos. | `constitution.md`, `architecture/overview.md`, live `foundation/*.md` |
| `devspec.projectcontext.prompt.md` | Capture product vision, users, goals, non-goals, constraints, and metrics. | `foundation/project-context.md` |
| `devspec.techstack.prompt.md` | Capture languages, frameworks, services, tooling, hosting, and versions. | `foundation/tech-stack.md` |
| `devspec.codebase-structure.prompt.md` | Capture repo layout, module boundaries, ownership seams, and multi-repo config. | `foundation/codebase-structure.md` |
| `devspec.coding-standards.prompt.md` | Capture evidence-backed language/framework standards, observed patterns, source links, and short examples. | `foundation/coding-standards.md` |
| `devspec.rules.prompt.md` | Capture operational constraints, compliance, forbidden patterns, and gates. | `foundation/rules.md` |
| `devspec.story.prompt.md` | Create or update work-item intake artifacts. | `meta.md`, `story.md`, support files |
| `devspec.clarify.prompt.md` | Ask and record one blocking clarification. | `clarify.md` |
| `devspec.finalize.prompt.md` | Freeze an implementation-ready brief. | `finalize.md` |
| `devspec.tasks.prompt.md` | Break a ready brief into ordered implementation tasks. | `tasks.md` |
| `devspec.implement.prompt.md` | Implement pending tasks and record progress. | `implement.md`, code changes |
| `devspec.review.prompt.md` | Review implemented work against the finalized brief. | `review.md` |

## Maintenance

- Keep prompts stage-specific and concise.
- Keep agents focused on execution, tools, and handoffs.
- Put shared mechanics in `PATTERNS.md`.
- Put operational gates in `../../devspec/foundation/rules.md`.
- Update the matching prompt, agent, and `_template` contract together when a stage contract changes.
