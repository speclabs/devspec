# devspec

`devspec` is a spec-driven development framework for teams using GitHub Copilot and other AI coding agents.

It stores planning, implementation, review, and recovery state in Git-tracked files instead of relying on chat history.

Use it when you want agents to follow the same workflow for:

- project context, architecture, engineering rules, and coding standards
- feature, bug, and security work-item intake
- clarification, finalization, task planning, implementation, and review
- session recovery from repository artifacts

## Quick Start

Install with the `devspec` CLI. The recommended one-off path is `uvx`, which avoids a permanent global install and works well on machines where developers cannot write to shared PATH folders.

For install, workflow, AI coding agent, multi-repo, provider, validation, and upgrade examples, see [`docs/how-to/README.md`](docs/how-to/README.md).

1. Open the target repository in VS Code or the selected AI coding tool.
2. Install all supported adapter files into the repository:

   ```text
   uvx devspec init --target . --profile all --repo-state existing
   ```

   Use `--repo-state new` for a new repository.

3. Validate the install:

   ```text
   uvx devspec doctor --target . --profile all
   ```

4. Commit the copied files.
5. Run the foundation flow for a new or existing repository.
6. Start the first work item.

Manual copy remains supported as a fallback when package managers are blocked. Copy the framework folders listed in [Manual Copy Fallback](#manual-copy-fallback), then commit the copied files.

For a new project:

```text
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

For an existing project:

```text
/devspec.extract
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

Then run the work-item flow:

```text
/devspec.story
/devspec.finalize
/devspec.tasks
/devspec.implement
/devspec.review
```

Use `/devspec.clarify` only when a work item records a blocking question. Use `/devspec.diagram` when a diagram would clarify architecture, workflow, state, sequence, or domain behavior; SVG is the default, with optional Mermaid or HTML via `format=` combinations. Example: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`.

## How It Works

`devspec` has two workflow layers.

| Layer | Purpose | Commands |
| --- | --- | --- |
| Foundation | Capture stable project context, architecture, stack, structure, standards, and rules. | `/devspec.extract`, `/devspec.projectcontext`, `/devspec.techstack`, `/devspec.codebase-structure`, `/devspec.coding-standards`, `/devspec.rules` |
| Work items | Move one feature, bug, or security issue from intake to review. | `/devspec.story`, `/devspec.clarify`, `/devspec.finalize`, `/devspec.tasks`, `/devspec.implement`, `/devspec.review` |

```mermaid
flowchart TD
    Start["Start"] --> State{"Project state?"}
    State -- "new" --> ProjectContext["/devspec.projectcontext"]
    State -- "existing" --> Extract["/devspec.extract"]
    Extract --> ProjectContext
    ProjectContext --> TechStack["/devspec.techstack"]
    TechStack --> Structure["/devspec.codebase-structure"]
    Structure --> Standards["/devspec.coding-standards"]
    Standards --> Rules["/devspec.rules"]
    Rules --> Story["/devspec.story"]
    Story --> Blocked{"Blocking question?"}
    Blocked -- "yes" --> Clarify["/devspec.clarify"]
    Clarify --> Story
    Blocked -- "no" --> Finalize["/devspec.finalize"]
    Finalize --> Ready{"Ready?"}
    Ready -- "no" --> Clarify
    Ready -- "yes" --> Tasks["/devspec.tasks"]
    Tasks --> Implement["/devspec.implement"]
    Implement --> Review["/devspec.review"]
    Review --> Outcome{"Review outcome?"}
    Outcome -- "changes requested" --> Implement
    Outcome -- "approved" --> Done["Done"]
```

## Command Reference

| Command | Use when | Main output |
| --- | --- | --- |
| `/devspec.extract` | Existing code/docs should seed the foundation. | Foundation, architecture, extraction, and diagram queue artifacts. |
| `/devspec.projectcontext` | Product and business context must be recorded; durable principles and operational governance route to their own artifacts. | `devspec/foundation/project-context.md` |
| `/devspec.techstack` | Stack, runtime, hosting, tooling, or support status must be recorded. | `devspec/foundation/tech-stack.md` |
| `/devspec.codebase-structure` | Repository layout, boundaries, multi-repo access, or integration contracts must be recorded. | `devspec/foundation/codebase-structure.md` |
| `/devspec.coding-standards` | Engineering standards and observed patterns must be recorded. | `devspec/foundation/coding-standards.md` |
| `/devspec.rules` | Operational rules, compliance requirements, governance procedures, and gates must be recorded. | `devspec/foundation/rules.md` |
| `/devspec.story` | A feature, bug, security issue, task, PBI, or provider reference needs intake. | Work-item `meta.md`, `story.md`, `decisions.md`, `notes.md` |
| `/devspec.clarify` | A blocking question must be resolved. | Work-item `clarify.md` |
| `/devspec.finalize` | A work item needs an implementation-ready brief. | Work-item `finalize.md` |
| `/devspec.tasks` | A ready brief needs executable tasks. | Work-item `tasks.md` |
| `/devspec.implement` | Pending tasks should be implemented and recorded. | Work-item `implement.md` and code changes when applicable |
| `/devspec.review` | Implemented work needs review against the finalized brief. | Work-item `review.md` |
| `/devspec.diagram` | A diagram should be created or updated. | Architecture or work-item SVG diagram artifacts by default, with optional Mermaid or HTML artifacts |

For exact command contracts, see `devspec/adapters/command-registry.md`.

## AI Tool Support

GitHub Copilot prompt and agent files are the reference implementation. Other adapters are thin wrappers around the same command registry and Git-tracked artifacts.

| Tool | Files | Notes |
| --- | --- | --- |
| GitHub Copilot | `.github/prompts/`, `.github/agents/`; optional `.github/skills/` | Native `/devspec.*` command implementation. |
| Claude Code | `.claude/skills/devspec-*/SKILL.md` | Project skills for canonical commands. |
| OpenAI Codex | `AGENTS.md`, `devspec/adapters/codex.md` | Repository instructions and Codex guidance. |
| Cursor | `.cursor/rules/devspec-workflow.mdc`, `AGENTS.md` | Project rules plus shared fallback instructions. |
| Gemini CLI | `GEMINI.md`, optional `.gemini/commands/devspec/*.toml` | `GEMINI.md` is enough for context; TOML files only add native `/devspec:*` shortcuts. |
| Google Antigravity | `.agents/rules/devspec-workflow.md`, `.agents/skills/devspec-*.md` | Workspace rule and skills using `/devspec-*` names. |

Canonical command names remain `/devspec.*`. Some adapters expose host-native shortcuts such as `/devspec:story` or `/devspec-story`.

Related docs:

- [`docs/how-to/README.md`](docs/how-to/README.md)
- [`devspec/adapters/README.md`](devspec/adapters/README.md)
- [`devspec/adapters/compatibility-matrix.md`](devspec/adapters/compatibility-matrix.md)
- [`devspec/adapters/validation-flows.md`](devspec/adapters/validation-flows.md)
- [`devspec/adapters/enterprise-governance.md`](devspec/adapters/enterprise-governance.md)

## Repository Layout

| Path | Purpose |
| --- | --- |
| `devspec/constitution.md` | Rare durable project principles across all work items and agents; principle changes require explicit confirmation. |
| `devspec/foundation/` | Product context, stack, structure, standards, operational rules, exclusions, and provider policy. |
| `devspec/architecture/` | Architecture overview, default SVG diagrams, optional Mermaid or HTML diagrams, ADR templates, and artifact queue. |
| `devspec/work-items/` | One folder per feature, bug, or security work item. |
| `devspec/adapters/` | Multi-agent registry, compatibility, validation, and governance docs. |
| `docs/how-to/` | User manual with install, workflow, AI coding agent, multi-repo, provider, validation, and upgrade examples. |
| `.github/prompts/` | Copilot slash-command prompts. |
| `.github/agents/` | Copilot agent definitions. |
| `.github/skills/` | Optional reusable skills. |
| `AGENTS.md` | Shared instructions for tools that read `AGENTS.md`. |
| `GEMINI.md` | Gemini-native repository context. |
| `.claude/`, `.cursor/`, `.gemini/`, `.agents/` | Optional adapter support. |

## Manual Copy Fallback

Use manual copy only when the CLI, `uvx`, package managers, and release ZIP automation are blocked. Copy these core framework files and folders from the `devspec` release into the target repository root:

```text
devspec/
.github/prompts/
.github/agents/
AGENTS.md
```

Then copy only the adapter files your team uses:

| Tool | Additional files |
| --- | --- |
| GitHub Copilot | `.github/skills/` |
| Claude Code | `.claude/` |
| OpenAI Codex | No extra files beyond `AGENTS.md` |
| Cursor | `.cursor/` |
| Gemini CLI | `GEMINI.md`, `.gemini/` |
| Google Antigravity | `.agents/` |

The release payload may also include this repository's `README.md` and `docs/how-to/` for reference. Do not copy them into the target repository as installed framework files, and do not overwrite a target project's root `README.md`. Keep credentials, provider tokens, local auth files, and personal settings outside copied framework files.

Do not copy `.github/workflows/` into target repositories. Those workflows are this framework repository's CI/release automation, and target projects should own their own CI/CD configuration.

## Operating Rules

- Keep `.github/prompts/*.prompt.md` and `.github/agents/*.agent.md` as the protected reference contracts.
- Keep adapter support additive; do not change command intent for another tool.
- Store workflow state in Git-tracked `devspec/` artifacts, not chat memory.
- Use `devspec/glossary.md` for status values.
- Use `devspec/foundation/codebase-structure.md` for repository access requirements.
- Keep product facts in `devspec/foundation/project-context.md`, durable principles in `devspec/constitution.md`, and operational gates, compliance rules, enforcement details, and evolving governance in `devspec/foundation/rules.md`.
- Keep secrets and provider credentials outside prompt, agent, adapter, and artifact files.
- Record blockers instead of guessing.
- Recommend only registered `/devspec.*` commands.

## Multi-Repo Work

For multi-repo systems, open one workspace or tool project that includes every repository agents should inspect, edit, test, or coordinate.

Record repository roles, local paths, access requirements, and boundaries in:

```text
devspec/foundation/codebase-structure.md
```

Access values are defined in:

```text
devspec/glossary.md#access-requirement-values
```

## Provider Integrations

Use provider integrations when `/devspec.story` should resolve GitHub, Jira, Azure DevOps, or other external work-item references.

Provider policy lives in:

```text
devspec/foundation/provider-integrations.md
```

Keep authentication outside prompt artifacts. Prefer read-only provider access unless write-back is explicitly required.

## Validation

Enterprise readiness requires these flows to pass for each supported adapter:

- new repository foundation flow
- existing repository extraction flow
- full story lifecycle
- cross-tool recovery from Git-tracked artifacts

Use:

```text
devspec/adapters/validation-flows.md
```

## Upgrade Notes

Use the CLI to inspect and apply framework upgrades:

```text
devspec diff --target .
devspec sync --target . --profile all --dry-run
devspec sync --target . --profile all
```

Framework-owned files may be replaced or diff-applied during upgrades:

- `.github/prompts/`
- `.github/agents/`
- `.github/skills/`
- adapter support folders
- `AGENTS.md`
- `GEMINI.md`
- `devspec/adapters/`
- `devspec/**/_template/`

The `.github/workflows/` directory is intentionally excluded from setup and sync. Those files are this repository's CI/release automation, and target projects should own their own CI/CD configuration.

Project-owned files should be migrated or merged, not overwritten:

- `devspec/foundation/*.md`
- `devspec/architecture/*.md`
- `devspec/architecture/diagrams/*.md`
- `devspec/architecture/images/*.svg`
- `devspec/architecture/html/*.html`
- `devspec/work-items/**`
- `devspec/constitution.md`
- `devspec/glossary.md`

## Recommended Adoption

1. Install into one target repository with `uvx devspec init --target . --profile all --repo-state existing`.
2. Run the foundation flow.
3. Complete one real feature work item.
4. Complete one real bug work item.
5. Add security-vulnerability flow validation if relevant.
6. Adjust foundation docs based on what the first runs teach the team.

## Deployment Development

When changing the installer, profile manifest, package metadata, or release automation, run:

```text
uv run pytest
powershell -ExecutionPolicy Bypass -File scripts/test-local-install.ps1
bash scripts/test-local-install.sh
```

Update `packaging/devspec-profiles.json` whenever adapter files are added, removed, or moved.

## License

This repository is released under the [Apache License 2.0](LICENSE).
