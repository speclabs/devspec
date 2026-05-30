# Platform Compatibility Matrix

Use this matrix when adding or reviewing adapter support. A platform limitation must be documented here instead of changing `devspec` command semantics.

| Capability | GitHub Copilot in VS Code | Claude Code | OpenAI Codex | Cursor | Future adapters |
| --- | --- | --- | --- | --- | --- |
| Reference status | Reference implementation | Adapter | Adapter | Adapter | Adapter |
| Native command surface | `.github/prompts/*.prompt.md` registers `/devspec.*` prompt files. | `.claude/skills/*/SKILL.md` project skills expose command-like workflows. | `AGENTS.md` provides always-on guidance; Codex slash commands are tool-owned and should not be assumed to mirror Copilot prompt files. | `.cursor/rules/*.mdc` provides project rules; exact custom slash parity is not assumed. | Must map to `devspec/adapters/command-registry.md`. |
| Agent surface | `.github/agents/*.agent.md` with tools, model fallback, and handoffs. | Skills may run inline or through Claude subagents when configured. | Skills and app or CLI features may assist, but the repo contract starts from `AGENTS.md`. | Cursor Agent applies project rules and referenced files. | Must preserve command intent and artifact contracts. |
| Always-on repository guidance | Optional `.github/copilot-instructions.md` or prompt/agent context. | `CLAUDE.md` may be used by adopters; this framework ships skills instead of changing memory. | Root `AGENTS.md`. | Root `AGENTS.md` plus `.cursor/rules`. | Prefer `AGENTS.md` when supported. |
| MCP or external tools | Supported through Copilot and configured VS Code tools. | Supported through Claude Code MCP configuration. | Supported through Codex MCP configuration when enabled by the environment. | Supported through Cursor MCP configuration when enabled by the environment. | Provider integrations must remain outside prompt artifacts. |
| Approval and permissions | Governed by VS Code, Copilot, workspace trust, and selected tools. | Governed by Claude Code permissions and tool approvals. | Governed by Codex local, cloud, sandbox, and approval settings. | Governed by Cursor Agent permissions and workspace settings. | Must document permissions before write workflows. |
| Telemetry | Use tool-provided telemetry when available; otherwise record unavailable in artifacts. | Use available session, cost, or tool data when exposed. | Use available Codex status or analytics data when exposed. | Use available Cursor session signals when exposed. | Missing telemetry is recorded as unavailable, not invented. |
| Known gaps | None for the current reference workflow. | Exact dotted `/devspec.*` command names may depend on skill or command naming behavior. | Copilot prompt files do not automatically register as Codex slash commands. | Cursor rules guide behavior but do not guarantee slash-command registration. | Must be captured before enterprise rollout. |

## Compatibility Rules

- Keep command names and artifact contracts stable even when the host tool uses a different invocation surface.
- Prefer explicit user invocation for stage commands that write artifacts or code.
- Do not store credentials, tokens, personal settings, or provider secrets in adapter files.
- Record unsupported host features as platform gaps and continue to use the canonical `devspec` artifacts.
