# Devspec Prompt Index

This folder contains the user-facing slash-command prompt definitions for the devspec workflow.

Use this file as an index, not as a second source of behavioral truth.

## Workflow

Foundation flow:

1. `devspec.extract` or start manually
2. `devspec.projectcontext`
3. `devspec.techstack`
4. `devspec.codebase-structure`
5. `devspec.coding-standards`
6. `devspec.rules`

Work-item flow:

1. `devspec.story`
2. `devspec.clarify`
3. `devspec.finalize`
4. `devspec.tasks`
5. `devspec.implement`
6. `devspec.review`

## Shared References

- `PATTERNS.md`: shared interaction, prerequisite, output, and multi-repo handling rules.
- `../../devspec/foundation/rules.md`: canonical bug and security workflow rules.
- `../../devspec/foundation/codebase-structure.md`: single source of truth for multi-repo configuration.
- `../../devspec/work-items/_template/`: durable output shapes for work-item artifacts.

## Foundation Prompts

### `devspec.extract.prompt.md`

- Purpose: derive constitution candidates, architecture context, and foundation artifacts from one or more repositories.
- Produces: updates under `devspec/constitution.md`, `devspec/architecture/overview.md`, and `devspec/foundation/`.
- Notes: must confirm constitution changes before writing them.

### `devspec.projectcontext.prompt.md`

- Purpose: capture product vision, users, goals, non-goals, and business constraints.
- Produces: `devspec/foundation/project-context.md`.

### `devspec.techstack.prompt.md`

- Purpose: capture languages, frameworks, services, tooling, hosting, and delivery constraints.
- Produces: `devspec/foundation/tech-stack.md`.

### `devspec.codebase-structure.prompt.md`

- Purpose: capture repository layout, module boundaries, ownership seams, and multi-repo configuration.
- Produces: `devspec/foundation/codebase-structure.md`.

### `devspec.coding-standards.prompt.md`

- Purpose: capture direct standards, linked standards, or repository-local standards by language or framework.
- Produces: `devspec/foundation/coding-standards.md`.

### `devspec.rules.prompt.md`

- Purpose: capture hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates.
- Produces: `devspec/foundation/rules.md`.

## Work-Item Prompts

### `devspec.story.prompt.md`

- Purpose: create or update the work-item intake artifacts.
- Produces: `meta.md`, `story.md`, and initial support files.
- Notes: validates provider input, confirms resolved details, and checks multi-repo configuration before intake continues.

### `devspec.clarify.prompt.md`

- Purpose: ask and record exactly one blocking clarification at a time.
- Produces: `clarify.md`.

### `devspec.finalize.prompt.md`

- Purpose: freeze the work item into an implementation-ready brief.
- Produces: `finalize.md` with `ready` or `not ready` status.

### `devspec.tasks.prompt.md`

- Purpose: break a ready work item into ordered implementation tasks without changing scope.
- Produces: `tasks.md`.

### `devspec.implement.prompt.md`

- Purpose: implement pending tasks sequentially, confirm whether to continue after each task, and record progress.
- Produces: `implement.md` and code changes when applicable.

### `devspec.review.prompt.md`

- Purpose: review the implemented work item against the finalized brief.
- Produces: `review.md` with approval or change-request status.

## Agent Pairing

Each prompt has a same-named agent under `../agents/`.

- Prompts define slash-command entry points and required user input.
- Agents define runtime behavior, available tools, and handoffs.
- Shared behavior belongs in `PATTERNS.md` or canonical foundation artifacts instead of being duplicated in every prompt-agent pair.

## Maintenance Rules

- Keep prompt files focused on stage-specific behavior.
- Keep agent files focused on execution behavior and handoffs.
- Add shared workflow mechanics to `PATTERNS.md` instead of repeating them.
- Add bug or security workflow rules to `../../devspec/foundation/rules.md` instead of scattering them across prompts, agents, and templates.
- Update the matching prompt, agent, and output template together when a stage contract changes.
