# Multi-Agent Adapter Guide

Use this directory to keep multi-agent support additive. Existing Copilot prompt and agent files remain the reference implementation; adapters for Claude Code, OpenAI Codex, Cursor, Gemini CLI, Google Antigravity, and future tools must preserve their intent instead of redefining the workflow.

## Adapter Contract

| Contract area | Requirement |
| --- | --- |
| Reference source | Use `.github/prompts/*.prompt.md` and `.github/agents/*.agent.md` as the canonical command and agent contracts. |
| Command registry | Use `devspec/adapters/command-registry.md` for provider-neutral command names, required inputs, outputs, mutation levels, and handoffs. |
| State source | Recover from Git-tracked `devspec/` artifacts before relying on chat history or tool memory. |
| Intent preservation | Do not change command purpose, required input, output artifacts, status values, handoff order, readiness gates, review gates, or recovery behavior. |
| Platform gaps | Document unsupported behavior as a limitation; do not hide gaps by changing `devspec` semantics. |
| Integration model | Keep provider lookup, CI, scanners, and enterprise systems behind MCP servers or equivalent internal tools. |

## Adapter Files

| Adapter | Primary files | Role |
| --- | --- | --- |
| GitHub Copilot | `.github/prompts/`, `.github/agents/`, `.github/skills/` | Native `/devspec.*` command implementation and reference adapter. |
| Claude Code | `.claude/skills/devspec-*/SKILL.md` | Project skills that invoke the same command contract from Claude Code. |
| OpenAI Codex | `AGENTS.md`, `devspec/adapters/codex.md` | Always-on repository guidance and Codex usage notes for the same workflow. |
| Cursor | `.cursor/rules/devspec-workflow.mdc`, `AGENTS.md` | Project rule guidance for Cursor Agent and Inline Edit. |
| Gemini CLI | `GEMINI.md`, `.gemini/commands/devspec/*.toml` | Gemini context and project custom commands for the same workflow. |
| Google Antigravity | `.agents/rules/devspec-workflow.md`, `.agents/skills/devspec-*.md` | Workspace rule and skills for Antigravity agents. |
| Future tools | `devspec/adapters/command-registry.md`, `AGENTS.md` | Map new tool-specific commands, skills, or rules to the same registry. |

## Usage Examples

For install steps, workflow walkthroughs, and copy-ready command examples across AI coding agents, see [`../../docs/how-to/README.md`](../../docs/how-to/README.md).

## Implementation Order

1. Confirm the command exists in `devspec/adapters/command-registry.md`.
2. Read the canonical Copilot prompt and agent files named in the registry.
3. Implement a thin adapter wrapper for the target tool.
4. Preserve artifact writes, gates, and next-action behavior.
5. Validate with `devspec/adapters/validation-flows.md`.

## No-Intent-Drift Rules

An adapter has drifted when it does any of the following:

- changes the purpose of a command or stage
- drops a required input or confirmation
- writes a different artifact set
- relaxes readiness, review, repository-access, or security gates
- renames or invents status values outside `devspec/glossary.md`
- changes the registered next command or handoff order
- treats platform-specific limitations as workflow changes
- relies on chat memory when a Git-tracked `devspec` artifact exists

If exact behavior cannot be represented on a platform, record the gap in `devspec/adapters/compatibility-matrix.md` and keep the workflow contract unchanged.
