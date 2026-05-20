# devspec

`devspec` is a spec-driven development framework for developers using GitHub Copilot Chat.

It gives your repository:

- a canonical place for project principles, architecture, and engineering rules
- a repeatable command flow for turning work items into implementation-ready specs
- durable artifacts for story intake, clarification, finalization, task planning, implementation, and review

In short: `devspec` helps teams define the spec before coding, keep implementation aligned to that spec, and leave a reviewable paper trail in Git.

## What devspec adds to a repository

When installed into a project, `devspec` adds three kinds of assets:

1. `devspec/`
   This is the canonical source of truth for project context, architecture, rules, and work-item artifacts.

2. `.github/prompts/` and `.github/agents/`
   These power the GitHub Copilot Chat slash-command workflow such as `/devspec.extract`, `/devspec.projectcontext`, and `/devspec.story`.

3. `.github/skills/`
   Optional reusable GitHub-hosted skills for agent behaviors that should travel across repositories, such as exploration recovery.

## How devspec works

The workflow has two layers:

1. Project foundation
   Define the stable project context that every future story should follow.

2. Work-item execution
   Take one feature, bug, or security issue through intake, clarification, finalization, tasks, implementation, and review.

The intended command sequence is:

1. `/devspec.extract` for existing projects only, or when backfilling from an existing repo
2. `/devspec.projectcontext`
3. `/devspec.techstack`
4. `/devspec.codebase-structure`
5. `/devspec.coding-standards`
6. `/devspec.rules`
7. `/devspec.story`
8. `/devspec.clarify`
9. `/devspec.finalize`
10. `/devspec.tasks`
11. `/devspec.implement`
12. `/devspec.review`

## Setup

Right now, the recommended setup is file-copy based. Package-based install can be added later, but the current workflow assumes these files live inside the target repository.

Before you start:

- open the target repository as a workspace in VS Code
- for multi-repo work, open a VS Code multi-root workspace that includes every repo you expect to inspect, edit, test, or coordinate
- make sure GitHub Copilot Chat is available in that workspace
- copy both `.github/prompts/` and `.github/agents/` along with `devspec/`, because the slash-command workflow depends on all three
- optionally copy `.github/skills/` when you want agents to reuse the bundled skills directly

For multi-repo work, the most reliable pattern is to keep one shared workspace open and record repo configuration in `devspec/foundation/codebase-structure.md`. That keeps one source of truth for local repo paths and access requirements, so story, tasks, finalize, and implement rely on the same configured repos. Single-repo work does not need any extra repo configuration.

Do not directly overwrite project-owned artifacts during manual upgrades. Framework-owned files live under `.github/`, `devspec/**/_template/`, and prompt/agent support files. Live files such as `devspec/foundation/*.md`, `devspec/architecture/*.md`, `devspec/constitution.md`, and `devspec/glossary.md` are project-owned and should be migrated or merged.

Manual upgrade ownership:

| Path | Owner | Upgrade action |
| --- | --- | --- |
| `.github/skills/` | framework | Replace or diff-apply |
| `.github/agents/` | framework | Replace or diff-apply |
| `.github/prompts/` | framework | Replace or diff-apply |
| `devspec/**/_template/` | framework | Replace or diff-apply |
| `devspec/architecture/decisions/_template.md` | framework | Replace or diff-apply |
| `devspec/foundation/*.md` | project | Do not overwrite; migrate or merge |
| `devspec/architecture/*.md` | project | Do not overwrite; migrate or merge |
| `devspec/constitution.md` | project | Do not overwrite; confirmation required |
| `devspec/glossary.md` | project | Do not overwrite; migrate or merge |

Installation worked if:

- the copied files are visible in the target repository under `devspec/`, `.github/prompts/`, and `.github/agents/`
- if copied, `.github/skills/exploration-recovery/SKILL.md` is visible in the target repository
- `.github/prompts/PATTERNS.md` is present, because every prompt and agent relies on the shared patterns there
- GitHub Copilot Chat in that repository recognizes `/devspec` commands such as `/devspec.projectcontext` or `/devspec.story`

If the commands do not appear, reopen the repository workspace in VS Code and confirm the prompt and agent files were copied into the target repository root rather than a nested folder.

### What to copy into the target repo

Use this minimal working structure:

```text
your-repo/
|-- .github/
|   |-- agents/
|   |   |-- devspec.clarify.agent.md
|   |   |-- devspec.codebase-structure.agent.md
|   |   |-- devspec.coding-standards.agent.md
|   |   |-- devspec.extract.agent.md
|   |   |-- devspec.finalize.agent.md
|   |   |-- devspec.implement-task.agent.md
|   |   |-- devspec.projectcontext.agent.md
|   |   |-- devspec.review.agent.md
|   |   |-- devspec.rules.agent.md
|   |   |-- devspec.story.agent.md
|   |   |-- devspec.tasks.agent.md
|   |   `-- devspec.techstack.agent.md
|   |-- prompts/
|   |   |-- PATTERNS.md
|   |   |-- README.md
|   |   |-- devspec.clarify.prompt.md
|   |   |-- devspec.codebase-structure.prompt.md
|   |   |-- devspec.coding-standards.prompt.md
|   |   |-- devspec.extract.prompt.md
|   |   |-- devspec.finalize.prompt.md
|   |   |-- devspec.implement.prompt.md
|   |   |-- devspec.projectcontext.prompt.md
|   |   |-- devspec.review.prompt.md
|   |   |-- devspec.rules.prompt.md
|   |   |-- devspec.story.prompt.md
|   |   |-- devspec.tasks.prompt.md
|   |   `-- devspec.techstack.prompt.md
|   `-- skills/
|       `-- exploration-recovery/
|           `-- SKILL.md
`-- devspec/
    |-- constitution.md
    |-- glossary.md
    |-- architecture/
    |   |-- _template/
    |   |   |-- artifact-queue.md
    |   |   `-- overview.md
    |   |-- artifact-queue.md
    |   |-- overview.md
    |   `-- decisions/
    |       |-- README.md
    |       `-- _template.md
    |-- foundation/
    |   |-- _template/
    |   |   |-- project-context.md
    |   |   |-- tech-stack.md
    |   |   |-- codebase-structure.md
    |   |   |-- coding-standards.md
    |   |   |-- discovery-exclusions.md
    |   |   |-- exploration-state.md
    |   |   |-- provider-integrations.md
    |   |   `-- rules.md
    |   |-- project-context.md
    |   |-- tech-stack.md
    |   |-- codebase-structure.md
    |   |-- coding-standards.md
    |   |-- discovery-exclusions.md
    |   |-- exploration-state.md
    |   |-- provider-integrations.md
    |   `-- rules.md
    `-- work-items/
        `-- _template/
            |-- meta.md
            |-- story.md
            |-- clarify.md
            |-- finalize.md
            |-- tasks.md
            |-- implement.md
            |-- review.md
            |-- decisions.md
            `-- notes.md
```

### Setup on a new project

For a brand-new repository with little or no existing code:

1. Copy these folders into the target repo:
   - `devspec/`
   - `.github/prompts/`
   - `.github/agents/`
   - `.github/skills/` when you want reusable agent skills
2. Commit the copied files.
3. Open the repository in GitHub Copilot Chat.
4. Start the foundation workflow with `/devspec.projectcontext`.

For a new project, you will usually skip `/devspec.extract` because there is no mature codebase to backfill yet.

On first install, live project artifacts may be created from the matching `_template` files. After that, treat the live files as project-owned and update them through the slash-command workflow rather than replacing them from a newer template.

### Setup on an existing project

For an existing application or monorepo:

1. Copy these folders into the target repo:
   - `devspec/`
   - `.github/prompts/`
   - `.github/agents/`
   - `.github/skills/` when you want reusable agent skills
2. Commit the copied files.
3. Open the repository in GitHub Copilot Chat.
4. Start with `/devspec.extract` and point it at the current repository path or repository URL.
5. Refine the extracted foundation using the remaining foundation commands.

This path is best when you already have source code, docs, manifests, CI config, or architecture clues that can be mined into `devspec`.

## Recommended foundation sequences

### New project sequence

For a new project with little code, use:

1. `/devspec.projectcontext`
2. `/devspec.techstack`
3. `/devspec.codebase-structure`
4. `/devspec.coding-standards`
5. `/devspec.rules`

You can then manually refine:

- `devspec/constitution.md`
- `devspec/architecture/overview.md`

Or let those evolve as the project becomes more concrete.

### Existing project sequence

For an existing project, use:

1. `/devspec.extract`
2. `/devspec.projectcontext`
3. `/devspec.techstack`
4. `/devspec.codebase-structure`
5. `/devspec.coding-standards`
6. `/devspec.rules`

This gives you evidence-backed foundation docs first, then lets you refine them with business and operational context that source code alone cannot supply.

## Important workflow rules

These are core behaviors baked into the prompts and agents:

- Foundation commands require user input.
- `/devspec.story` requires user input.
- Later work-item commands accept optional additive input.
- Clarification should happen one question at a time.
- Clarification, confirmation, selection, retry, queue, and continuation questions should use explicit options plus `Custom Answer`, with exactly one recommended option and a short justification.
- Recommended next steps must be singular. Agents should not list multiple possible next prompts when one confirmation, queue item, handoff, retry, or fallback decision is pending.
- Agents must recommend only registered devspec slash commands. Do not use inferred commands such as `/devspec.plan`; planning work maps to `/devspec.tasks`.
- `/devspec.extract` must not silently rewrite `constitution.md` principles from code inference alone.
- Repository discovery must exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output paths by default; for Node.js projects, use `package.json`, lockfiles, and framework config as evidence instead of searching `node_modules/`.
- Discovery-heavy commands should check `devspec/foundation/exploration-state.md`, use known working methods first, and skip known failed searches, scripts, helper commands, provider lookups, or validation probes unless retry conditions are met.
- `/devspec.finalize` should mark a story `not ready` if blockers remain.
- `/devspec.tasks` must not expand scope.
- `/devspec.implement` should implement pending tasks sequentially, then ask one structured `Proceed`, `Skip`, or `Custom Answer` question after each task.
- `/devspec.review` should review against the finalized brief, not re-plan the story.

## Foundation workflow

These commands establish the project-wide spec that all stories must follow.

### 1. `/devspec.extract`

Use this when you already have a repository and want Copilot to backfill `devspec` from source code and existing docs.

What it does:

- validates repository URLs or local repository paths
- reads repository layout, manifests, CI/CD, docs, config, style guides, ADRs, contribution docs, and related evidence
- excludes dependency and generated folders such as `node_modules/`, `.angular/`, `dist/`, `build/`, and `coverage/` unless the project records an explicit override
- prefers direct repository search and known working exploration methods before trying new generated scripts
- proposes updates to:
  - `devspec/constitution.md`
  - `devspec/architecture/overview.md`
  - live `devspec/foundation/*.md` artifacts, excluding `devspec/foundation/_template/`
- requires explicit confirmation before writing principle-level changes to `constitution.md`
- asks only one structured extraction confirmation at a time; constitution confirmation, artifact-queue approval, and Mermaid generation approval must not be asked together
- processes artifact-queue items one at a time in queue order, asking one structured question for the next unresolved item only
- closes with one next action or one structured question, not a list of possible next prompts

Use it for:

- existing products
- monorepos
- migrations where architecture and standards already exist but are undocumented

Example:

```text
/devspec.extract D:\code\payments-platform
```

Another example:

```text
/devspec.extract https://github.com/acme/payments-platform
```

Expected outcome:

- `architecture/overview.md` gets a first-pass system view
- `foundation/tech-stack.md` gets stack evidence
- `foundation/codebase-structure.md` gets a repo-layout draft
- repository layout should be a selective 3-5 level map that helps agents place new files and folders
- `foundation/coding-standards.md` gets evidence-backed language-specific and framework-specific standards when the repository exposes them
- `foundation/rules.md` gets evidence-backed candidate content
- `constitution.md` gets only confirmed principle updates

### 2. `/devspec.projectcontext`

Use this to create or refine the canonical project brief.

What it writes:

- `devspec/foundation/project-context.md`

Use it for:

- defining product vision
- identifying users and stakeholders
- recording goals, non-goals, and business constraints

Example:

```text
/devspec.projectcontext Build a B2B invoice approval platform for finance teams. Primary users are AP clerks and finance managers. Goals are faster approval turnaround and auditability. Non-goals include payroll and tax filing. Constraints include SOC 2, role-based access control, and a six-week MVP timeline.
```

### 3. `/devspec.techstack`

Use this to define the real technical environment.

What it writes:

- `devspec/foundation/tech-stack.md`

Use it for:

- languages and runtimes
- frameworks and libraries
- services and infrastructure
- build, test, lint, CI/CD, and hosting choices

Example:

```text
/devspec.techstack Frontend uses Next.js 15 with TypeScript. Backend uses Node.js 22 and PostgreSQL 16. Auth is Auth0. Hosting is Vercel plus AWS RDS. CI runs in GitHub Actions. Tests use Playwright and Vitest.
```

### 4. `/devspec.codebase-structure`

Use this to describe how the repository is organized.

What it writes:

- `devspec/foundation/codebase-structure.md`

Use it for:

- repo tree
- multi-repo repo configuration when applicable
- module boundaries
- ownership seams
- integration boundaries

For multi-repo projects, use this stage to capture each repo's role, local path, whether it is already open in the current VS Code workspace, and its access requirement such as `reference-only`, `edit`, `edit-and-test`, `validation-only`, `release-coordination`, or `blocked`.

Agents must not assume `reference-only` or any other access requirement. When a repo access requirement is missing or ambiguous, the agent should ask one multiple-choice confirmation for that repo before writing or relying on the repo configuration.

Repos outside the current repo folder are valid multi-repo participants. Their location should not imply `reference-only`; record the local path, workspace availability, and user-confirmed access requirement separately.

The repository tree should go deep enough for file-placement decisions, usually 3-5 levels for important source roots, feature/module folders, tests, scripts, config, infrastructure, docs, and routing-critical files. Avoid exhaustive file listings.

Example:

```text
/devspec.codebase-structure Monorepo with apps/web for the customer UI, apps/admin for internal tools, packages/ui for shared components, packages/config for lint and tsconfig presets, and services/api for backend APIs. Payments logic must stay inside services/api/modules/payments.
```

### 5. `/devspec.coding-standards`

Use this to capture how the team expects code to be written.

What it writes:

- `devspec/foundation/coding-standards.md`

Use it for:

- language-specific or framework-specific coding standards
- naming and style rules
- database or SQL indentation patterns
- member grouping and ordering rules when the team provides, confirms, or the repository clearly evidences them
- documentation-comment expectations where supported, and developer comments for non-obvious implementation details
- testing expectations
- error handling
- logging and observability
- review expectations
- links to existing coding standards docs
- evidence-backed pattern catalogs with source paths and confidence
- short canonical examples for important style, indentation, SQL layout, member ordering, or framework patterns when available

Example:

```text
/devspec.coding-standards Prefer explicit TypeScript types at module boundaries. Require unit tests for business logic and Playwright coverage for critical user flows. Use structured logging with request ids. Avoid silent catch blocks. Require concise developer comments for non-obvious implementation details. Document any new environment variables in the repo docs.
```

Another example:

```text
/devspec.coding-standards Use the existing standards in docs/engineering/csharp.md and https://example.com/python-style-guide for C# and Python. Confirm any gaps before writing.
```

### 6. `/devspec.rules`

Use this to define non-negotiable delivery constraints.

What it writes:

- `devspec/foundation/rules.md`

Use it for:

- compliance requirements
- forbidden libraries or patterns
- approval gates
- production readiness rules

Example:

```text
/devspec.rules PII must stay encrypted at rest and in transit. No client-side secrets. No ORM-generated schema changes without review. Production releases require passing CI, security scan approval, and rollback notes for database migrations.
```

## How to start a user story

Once the project foundation exists, use the work-item commands.

If you want `/devspec.story` to resolve GitHub, Jira, or Azure DevOps references, review and update `devspec/foundation/provider-integrations.md` first so the accepted provider formats, access model, and manual fallback are explicit for your repository.

The work-item flow is:

1. `/devspec.story`
2. `/devspec.clarify`
3. `/devspec.finalize`
4. `/devspec.tasks`
5. `/devspec.implement`
6. `/devspec.review`

### 1. `/devspec.story`

Use this to start or update a work item.

What it does:

- resolves a provider item when possible
- or supports manual intake when provider lookup is unavailable
- creates the work-item folder
- writes `meta.md` and `story.md`
- initializes `decisions.md` and `notes.md` if the folder is new
- for features, records priority instead of severity
- confirms multi-repo dependencies and records all related repos when applicable
- does not store local repo paths
- if the work is multi-repo, requires multi-repo foundation configuration in `devspec/foundation/codebase-structure.md` before story intake can continue
- leaves local paths and repo access requirements in the foundation artifact rather than duplicating them into story artifacts

Supported inputs:

- GitHub issue URL
- Jira issue key or URL
- Azure DevOps work item URL
- issue, task, bug, or PBI reference when the provider can be resolved clearly

Before relying on those external references, confirm that `devspec/foundation/provider-integrations.md` reflects your configured providers and fallback path. If it does not, use manual intake until that file is updated.

Example with an external reference:

```text
/devspec.story https://github.com/acme/customer-portal/issues/1842
```

Example with manual-style input after fallback:

```text
/devspec.story INS-2041
```

If provider lookup succeeds, the command should show the resolved item summary and ask you to confirm before it writes the work item. The confirmation choices are `Confirm and continue`, `Reject and retry input`, `Switch to manual intake`, `Cancel`, and `Custom Answer`. A custom answer routes back through clarification and must not create or update the work-item folder until resolved.

### What gets created

The story stage creates a folder under `devspec/work-items/<feature-name>/`.

Example:

```text
devspec/work-items/document-upload-virus-scan/
```

During story intake, the command writes:

- `meta.md`
- `story.md`
- `decisions.md`
- `notes.md`

Later workflow stages add or update:

- `clarify.md`
- `finalize.md`
- `tasks.md`
- `implement.md`
- `review.md`

### 2. `/devspec.clarify`

Use this only to resolve blocking ambiguity.

What it writes:

- `devspec/work-items/<feature-name>/clarify.md`

Important behavior:

- asks exactly one blocking question at a time
- uses explicit clickable options for confirmations, selections, and workflow decisions
- includes `Custom Answer`
- includes one recommended option with a short justification
- waits for your answer before proceeding

Example:

```text
/devspec.clarify
```

### 3. `/devspec.finalize`

Use this to freeze the implementation-ready brief.

What it writes:

- `devspec/work-items/<feature-name>/finalize.md`

Important behavior:

- marks the item `ready` or `not ready`
- does not invent missing requirements
- records final scope, acceptance criteria, dependencies, risks, and validation approach
- for multi-repo work, verifies that `devspec/foundation/codebase-structure.md` contains the required repo configuration and user-confirmed access requirements
- should stay `not ready` if required multi-repo foundation configuration is missing or incomplete

Example:

```text
/devspec.finalize Ensure malware scanning happens synchronously before uploaded files become visible to end users.
```

### 4. `/devspec.tasks`

Use this to break a ready work item into implementation tasks.

What it writes:

- `devspec/work-items/<feature-name>/tasks.md`

Important behavior:

- must not change or expand the finalized scope
- should create ordered, implementation-oriented tasks
- should include validation steps and type-specific checks
- for multi-repo work, should assign each task to a target repo and use `devspec/foundation/codebase-structure.md` as the source of truth for local repo paths and user-confirmed access requirements

Example:

```text
/devspec.tasks Prioritize backend scanning and storage quarantine before any admin UI changes.
```

### 5. `/devspec.implement`

Use this to implement pending tasks with confirmation after each task.

What it writes:

- `devspec/work-items/<feature-name>/implement.md`

Important behavior:

- requires `finalize.md` to be `ready`
- requires `tasks.md`
- implements pending tasks sequentially until the work is completed or the user chooses to stop or skip
- for multi-repo work, uses the repo configuration in `devspec/foundation/codebase-structure.md` as the single source of truth for which physical repo path to change and what access is allowed
- validates required repo paths and access requirements before making code changes or running validation, and surfaces missing repo access as a blocker
- after each task, reports completed and pending counts and asks one structured question with `Proceed`, `Skip`, and `Custom Answer`
- once all tasks are implemented, records the completed task list and completion summary
- if the same task loops more than 3 times, explains the issue and asks one structured question with `Proceed`, `Skip`, and `Custom Answer`
- captures token-usage summary before implementation and after completion when runtime telemetry is available, and records when it is unavailable
- updates the execution log and next-task handoff
- for bug fixes, records focused before-fix and after-fix code snippets in `implement.md` for audit purposes only

Example:

```text
/devspec.implement Focus on the first backend task and include validation notes for quarantine behavior.
```

### 6. `/devspec.review`

Use this to review the implemented work against the finalized brief.

What it writes:

- `devspec/work-items/<feature-name>/review.md`

Important behavior:

- checks scope drift, bugs, regressions, security risks, missing validation, and missing tests
- returns `approved`, `approved-with-follow-ups`, or `changes-requested`

Example:

```text
/devspec.review Pay extra attention to regression risk around existing file upload flows.
```

## Command reference and step order

Before using `/devspec.story` with external work-item references, validate `devspec/foundation/provider-integrations.md` for the providers and fallback behavior your repository supports. There is no dedicated provider-integrations slash command; initialize it from `devspec/foundation/_template/provider-integrations.md` and maintain it manually when provider formats, tools, or fallback behavior change.

Registered devspec slash commands are limited to `/devspec.extract`, `/devspec.projectcontext`, `/devspec.techstack`, `/devspec.codebase-structure`, `/devspec.coding-standards`, `/devspec.rules`, `/devspec.story`, `/devspec.clarify`, `/devspec.finalize`, `/devspec.tasks`, `/devspec.implement`, and `/devspec.review`.

Do not recommend unregistered commands such as `/devspec.plan`, `/devspec.architecture`, `/devspec.provider-integrations`, `/devspec.queue`, or `/devspec.decisions`. If no registered command fits, recommend a concrete file update, handoff, or structured question.

| Step | Command | Use when | Requires | Main output | Next step |
| --- | --- | --- | --- | --- | --- |
| 0 | `/devspec.extract` | Existing repositories need foundation backfill from code and docs. | Repository URL or local repo path. | `constitution.md`, `architecture/overview.md`, live `foundation/*.md` | Refine with `/devspec.projectcontext`. |
| 1 | `/devspec.projectcontext` | Product and business context need to be created or updated. | Product vision, users, goals, non-goals, and constraints. | `foundation/project-context.md` | `/devspec.techstack` |
| 2 | `/devspec.techstack` | Technical environment needs to be recorded. | Languages, frameworks, services, tooling, hosting, and delivery constraints. | `foundation/tech-stack.md` | `/devspec.codebase-structure` |
| 3 | `/devspec.codebase-structure` | Repo layout, module boundaries, ownership seams, or multi-repo config need to be recorded. | Repository layout, integration boundaries, and multi-repo access requirements. | `foundation/codebase-structure.md` | `/devspec.coding-standards` |
| 4 | `/devspec.coding-standards` | Engineering expectations or observed code patterns need to be recorded. | Direct standards, links, repo-relative standards docs, or evidence-backed examples. | `foundation/coding-standards.md` | `/devspec.rules` |
| 5 | `/devspec.rules` | Operational hard constraints and delivery gates need to be recorded. | Compliance requirements, forbidden patterns, governance rules, and gates. | `foundation/rules.md` | `/devspec.story` |
| 6 | `/devspec.story` | A feature, bug, or security vulnerability needs intake. | Work-item reference or manual intake details. | `work-items/<feature-name>/meta.md`, `story.md`, `decisions.md`, `notes.md` | `/devspec.clarify` if blocked, otherwise `/devspec.finalize` |
| 7 | `/devspec.clarify` | A blocking question must be resolved. | Existing `story.md`. | `work-items/<feature-name>/clarify.md` | Repeat until unblocked, then `/devspec.finalize` |
| 8 | `/devspec.finalize` | The work item needs an implementation-ready brief. | Upstream work-item artifacts. | `work-items/<feature-name>/finalize.md` with `ready` or `not ready`. | `/devspec.tasks` when ready |
| 9 | `/devspec.tasks` | A ready brief needs ordered implementation tasks. | `finalize.md` marked `ready`. | `work-items/<feature-name>/tasks.md` | `/devspec.implement` |
| 10 | `/devspec.implement` | Pending tasks should be implemented. | `finalize.md` marked `ready` and `tasks.md`. | `work-items/<feature-name>/implement.md` and code changes when applicable. | `/devspec.review` |
| 11 | `/devspec.review` | Implemented work needs review against the finalized brief. | `finalize.md` and `implement.md`. | `work-items/<feature-name>/review.md` | Return to implementation for changes, or close the work item |

## End-to-end examples

### Example: new project

```text
/devspec.projectcontext Build a lightweight internal CRM for a small sales team. Users are account executives and sales managers. Goals are contact tracking, pipeline visibility, and activity logging. Non-goals include marketing automation and billing.
```

```text
/devspec.techstack Use React with TypeScript for the frontend, Node.js with Fastify for APIs, PostgreSQL for storage, and GitHub Actions for CI.
```

```text
/devspec.codebase-structure Single repo with src/web, src/api, src/shared, tests/e2e, and scripts. Shared validation schemas should live under src/shared/schemas.
```

```text
/devspec.coding-standards Require tests for pipeline calculations, structured logs for API errors, and short ADRs for durable architecture decisions.
```

```text
/devspec.rules No direct production database edits. Secrets must come from environment-specific secret stores. Schema changes need migration scripts and rollback notes.
```

Then start the first work item:

```text
/devspec.story CRM-12
```

### Example: existing project

```text
/devspec.extract D:\repos\warehouse-suite
```

```text
/devspec.projectcontext Warehouse operations suite for inventory control, receiving, putaway, and pick-pack-ship workflows. Users are warehouse associates, supervisors, and operations analysts. Goals are throughput, inventory accuracy, and operator efficiency.
```

```text
/devspec.techstack Confirm Node.js services, React frontend, PostgreSQL, Redis, Docker, GitHub Actions, and AWS deployment constraints.
```

Then start a story:

```text
/devspec.story https://github.com/acme/warehouse-suite/issues/932
```

## Repository layout

### `devspec/constitution.md`

Holds durable project principles that apply across all work items and all agents.

Examples:

- engineering principles
- delivery guardrails
- testing expectations
- security defaults

This file is intentionally harder to change. The extraction flow explicitly requires confirmation before principle-level updates are written.

### `devspec/foundation/`

Holds project-operational context and constraints.

- `_template/`
  Framework-owned section contracts for foundation artifacts. Installers and manual upgrades may update these files, but agents should write the live files below.
- `project-context.md`
  Product vision, intended users, goals, non-goals, constraints, and success metrics.
- `tech-stack.md`
  Languages, frameworks, services, tooling, hosting, current LTS versions, and delivery constraints.
- `codebase-structure.md`
  Repository layout, module boundaries, ownership seams, and integration boundaries.
- `coding-standards.md`
  Implementation expectations, testing rules, error handling, logging, documentation, and review norms.
- `discovery-exclusions.md`
  Default and project-specific paths agents should exclude from repository discovery, such as dependency, generated, build, cache, and coverage folders.
- `exploration-state.md`
  Known working and failed discovery methods for searches, scripts, provider lookups, validation probes, and extraction paths.
- `provider-integrations.md`
  Manually maintained provider intake policy for external systems such as GitHub, Jira, or Azure DevOps.
- `rules.md`
  Hard constraints, forbidden patterns, compliance rules, governance, and delivery gates.

### `devspec/architecture/`

Holds broader technical architecture.

- `_template/`
  Framework-owned section contracts for architecture artifacts. Use these to create or migrate live architecture files without overwriting project-specific content.
- `overview.md`
  System view, major components, integrations, data flow, and blockers.
- `decisions/`
  ADRs for long-lived architecture decisions.
- `decisions/_template.md`
  Framework-owned ADR template used when creating new architecture decision records.

### `devspec/work-items/`

Holds one folder per story, feature, bug, or security issue. Each work item carries its own staged artifacts from intake through review.

## Advanced: extracting information from an existing project

If you are adopting `devspec` into a working codebase, this is the most important setup flow.

### What `/devspec.extract` pulls from

The extract stage is designed to inspect:

- repository layout
- dependency manifests
- runtime and configuration surfaces
- CI/CD files
- infrastructure config
- contribution docs
- ADRs
- architecture docs
- CODEOWNERS and related ownership hints

The extract stage must not search dependency, generated, cache, coverage, build-output, VCS, or tool-output folders by default. For Node.js, Angular, React, Next, and Vite projects, use `package.json`, lockfiles, `angular.json`, `tsconfig*.json`, and framework config files as evidence instead of inspecting `node_modules/` or generated output.

### Where the extracted information goes

#### `devspec/constitution.md`

This should contain durable principles, not just observations. Extraction can propose principle-level content, but it should not finalize it without user confirmation.

Good extracted candidates:

- "Prefer small, reversible changes over broad rewrites"
- "Validation is required before work is considered complete"
- "Do not weaken security controls without explicit approval"

#### `devspec/architecture/overview.md`

This should receive observed and high-confidence architectural facts such as:

- major components
- system boundaries
- external integrations
- high-level data flow
- a resumable Mermaid work queue in `devspec/architecture/artifact-queue.md` for architecture diagrams and user journeys when high-level modules or workflows are identified
- confirmed Mermaid diagrams and user journeys, generated one at a time after user approval and never in the same response as constitution confirmation

Use `devspec/architecture/_template/overview.md` and `devspec/architecture/_template/artifact-queue.md` as section contracts. Do not replace live architecture files from templates after a project has recorded real architecture content.

#### `devspec/foundation/project-context.md`

This may get partial drafts from docs, but usually needs human input because product goals and intended outcomes are often not fully inferable from code.

Use `devspec/foundation/_template/project-context.md` as the section contract.

#### `devspec/foundation/tech-stack.md`

This is one of the strongest extraction targets because code and manifests usually reveal:

- languages
- runtimes
- frameworks
- databases
- current LTS versions when practical to verify
- hosting clues
- test tooling
- CI tooling

Use `devspec/foundation/_template/tech-stack.md` as the section contract.

#### `devspec/foundation/codebase-structure.md`

This is also a strong extraction target because folder layout and module names can usually be observed directly. Extracted layouts should be selective 3-5 level trees focused on helping agents decide where new files and folders belong. For multi-repo work, this file is also the source of truth for repo roles, local paths, workspace availability, and user-confirmed access requirements.

Use `devspec/foundation/_template/codebase-structure.md` as the section contract.

#### `devspec/foundation/discovery-exclusions.md`

This records default and project-specific paths that should be excluded from repository discovery. It protects token usage and prevents agents from inferring project architecture or coding standards from dependency folders, generated files, build outputs, coverage, caches, and local tool output.

Use `devspec/foundation/_template/discovery-exclusions.md` as the section contract.

#### `devspec/foundation/coding-standards.md`

This can be partially inferred from:

- lint config
- formatting config
- language-specific style config such as `.editorconfig`, StyleCop, ESLint, Prettier, Ruff, Black, Checkstyle, Spotless, or clang-format
- test patterns
- logging libraries
- existing conventions in the codebase
- standards docs or style-guide links already referenced by the repository

Useful extracted examples include short snippets that show the prevailing indentation or formatting pattern, especially for SQL query layout and other database code. Treat this file as a pattern catalog: record the rule, source evidence, confidence, and a compact example rather than copying large code blocks.

But the result should still be reviewed, because "what the code does today" and "what the team wants as a standard" are not always the same.

Use `devspec/foundation/_template/coding-standards.md` as the section contract.

#### `devspec/foundation/rules.md`

This may be partially supported by:

- CI checks
- branch policies
- security scanning
- deployment gates
- compliance docs

But project-operational rules often need human refinement after extraction.

Use `devspec/foundation/_template/rules.md` as the section contract.

### Practical existing-project example

Example sequence in Copilot Chat:

```text
/devspec.extract D:\work\customer-portal
```

Then refine what the code could not fully tell you:

```text
/devspec.projectcontext Customer portal for insurance members to view claims, upload documents, and track approvals. Primary users are policyholders and support agents. Goals are self-service and lower support volume. Non-goals include broker onboarding. Constraints include HIPAA-adjacent privacy expectations and mobile-first usage.
```

```text
/devspec.rules Protected health information must not be exposed in logs. Any document-upload change requires malware scanning and content-type validation. Releases need QA signoff for claims workflows.
```

## Advanced: setting up MCP servers or tools in VS Code

Use this setup when you want `devspec` to resolve external work items instead of falling back to manual intake.

1. Choose the provider access path you will support in VS Code.
   For most teams, this means an MCP server per provider or one internal tool that wraps multiple providers.
2. Install or connect that MCP server or integration tool in the VS Code environment your team uses for Copilot Chat.
3. Configure authentication outside the prompt artifacts.
   Prefer least-privilege, read-only access for story intake and review workflows unless write-back is explicitly required.
4. Verify the integration can validate and fetch a real work item before relying on `/devspec.story`.
   The integration should be able to return core fields such as title, description, status, type or labels, and canonical links.
5. Record the supported providers, accepted input formats, and manual fallback policy in `devspec/foundation/provider-integrations.md`.
   If the file is missing, initialize it from `devspec/foundation/_template/provider-integrations.md`.
6. Test one provider-backed intake example and one manual fallback example in the target repository.

You should treat provider-backed intake as ready only when VS Code can reach the configured tool, authentication works, and `devspec/foundation/provider-integrations.md` matches the behavior your team expects.

## Recommended adoption pattern

If you are introducing `devspec` to a team, this usually works well:

1. Install it into one target repo.
2. Run the foundation flow.
3. Start one real feature story.
4. Start one real bug story.
5. If relevant, run one security-vulnerability story.
6. Adjust the foundation docs after learning from those first runs.

## Current limitation

Setup is currently copy-based. There is no `npm`, package-manager, or installer-based bootstrap flow yet.

That is a reasonable future enhancement, but the current framework expects `devspec/`, `.github/prompts/`, and `.github/agents/` to exist directly in the target repository.

## License

This repository is released under the [Apache License 2.0](LICENSE).
See [LICENSE](LICENSE) for the full license text.
