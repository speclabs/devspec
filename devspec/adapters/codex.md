# OpenAI Codex Adapter

OpenAI Codex support starts with root `AGENTS.md`, which gives Codex the always-on repository instructions for the `devspec` workflow.

## Invocation Model

| Surface | Expected behavior |
| --- | --- |
| `AGENTS.md` | Teaches Codex to treat `/devspec.*` as workflow intent and to use the command registry before acting. |
| Codex CLI or IDE extension | Users may type the canonical command name in a prompt, but Copilot prompt files are not assumed to register as Codex slash commands. |
| Codex skills | Optional starter template lives at `devspec/adapters/codex-skills/devspec-workflow/SKILL.md`; any installed skill must remain a thin wrapper over `devspec/adapters/command-registry.md`. |

## Adapter Rules

- Read `AGENTS.md` and `devspec/adapters/command-registry.md` before executing a `devspec` workflow.
- Preserve Copilot prompt and agent intent from the canonical files listed in the registry.
- Use Git-tracked `devspec` artifacts for recovery and handoff decisions.
- `/devspec.diagram` defaults to SVG output. `format=` may contain any non-duplicated `+` combination of `svg`, `html`, and `mermaid`, such as `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, or `format=html+mermaid`, without creating a separate Codex command.
- Treat Codex-specific slash commands, local/cloud modes, sandboxing, and approvals as platform mechanics, not workflow changes.

## Validation

Run the flow checklists in `devspec/adapters/validation-flows.md` with Codex local workflows before using Codex for enterprise delivery.
