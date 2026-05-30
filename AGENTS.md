# Devspec Agent Instructions

Use these instructions for OpenAI Codex, Cursor, Gemini CLI, Google Antigravity, and other agents that read `AGENTS.md`.

## Canonical Workflow

`devspec` is a spec-driven development framework. The Git-tracked `devspec/` artifacts are the durable source of truth; chat history and tool memory are transient.

Before running or continuing any `devspec` workflow:

1. Read `devspec/adapters/command-registry.md` for the requested command.
2. Read the canonical Copilot prompt and agent files named in that registry row.
3. Follow `.github/prompts/PATTERNS.md` for shared workflow, recovery, output, discovery, and recommendation behavior.
4. Recover from existing `devspec/` artifacts before relying on memory.
5. Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.

## Structured Questions

Follow `.github/prompts/PATTERNS.md#interactive-question-pattern` for user questions. Use clickable multiple-choice options when the host supports them; otherwise render the same option labels as text and ask the user to reply with one label or `Custom Answer`. Preserve question intent, option labels, the recommended option, and the continuation condition in the relevant `Resume State` or `Workflow State` before waiting for input.

## No Intent Drift

Do not change the original intent of `.github/prompts/*.prompt.md` or `.github/agents/*.agent.md`.

An adapter or agent must not:

- change command purpose
- skip required input or confirmation
- write a different artifact set
- relax readiness, review, access, or security gates
- invent status values outside `devspec/glossary.md`
- recommend unregistered commands
- hide platform limitations by changing workflow semantics

Record platform gaps in `devspec/adapters/compatibility-matrix.md` when needed.

## Required Flows

New repository foundation:

```text
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

Existing repository foundation:

```text
/devspec.extract
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

Work-item story lifecycle:

```text
/devspec.story
/devspec.finalize
/devspec.tasks
/devspec.implement
/devspec.review
```

Use `/devspec.clarify` only when work-item intake or finalization records a blocking question. Use `/devspec.diagram` for diagram work after relevant context exists.

## Enterprise Validation

Use `devspec/adapters/validation-flows.md` as the acceptance checklist for new repository, existing repository, story lifecycle, and cross-tool recovery validation.

## Gemini and Antigravity Notes

- Gemini CLI reads `GEMINI.md`, which imports this file and maps native `/devspec:*` commands to canonical `/devspec.*` workflow intent.
- Google Antigravity reads workspace rules and skills from `.agents/`; native skills use `/devspec-*` names while preserving canonical `/devspec.*` command behavior.
- Gemini and Antigravity adapters must document platform-specific permission, sandbox, telemetry, and command-name limitations without changing `devspec` semantics.
