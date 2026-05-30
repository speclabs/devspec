# Cursor Adapter

Cursor support is implemented through project rules under `.cursor/rules/` and the shared root `AGENTS.md`.

## Invocation Model

| Surface | Expected behavior |
| --- | --- |
| `.cursor/rules/devspec-workflow.mdc` | Provides project-scoped guidance for Cursor Agent and Inline Edit. |
| `AGENTS.md` | Provides a simple cross-agent fallback for `devspec` workflow behavior. |
| Chat prompt | Users may type canonical `/devspec.*` command names as workflow intent; exact slash registration is not assumed. |

## Adapter Rules

- Use `devspec/adapters/command-registry.md` for command order, required input, artifact outputs, mutation level, and handoff.
- Preserve GitHub Copilot prompt and agent intent from the canonical files named in the registry.
- Do not let Cursor-specific memories or user rules override Git-tracked `devspec` artifacts.
- Record unsupported Cursor behavior in `devspec/adapters/compatibility-matrix.md`.

## Validation

Run the new repository, existing repository, story, and cross-tool recovery flows in `devspec/adapters/validation-flows.md` before treating Cursor as enterprise-ready.
