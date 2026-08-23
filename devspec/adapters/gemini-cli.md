# Gemini CLI Adapter

Gemini CLI support is implemented through root `GEMINI.md` plus project custom commands under `.gemini/commands/devspec/`.

## Invocation Model

| Devspec command | Gemini CLI command |
| --- | --- |
| `/devspec.extract` | `/devspec:extract` |
| `/devspec.projectcontext` | `/devspec:projectcontext` |
| `/devspec.techstack` | `/devspec:techstack` |
| `/devspec.codebase-structure` | `/devspec:codebase-structure` |
| `/devspec.coding-standards` | `/devspec:coding-standards` |
| `/devspec.rules` | `/devspec:rules` |
| `/devspec.story` | `/devspec:story` |
| `/devspec.changerequest` | `/devspec:changerequest` |
| `/devspec.clarify` | `/devspec:clarify` |
| `/devspec.finalize` | `/devspec:finalize` |
| `/devspec.tasks` | `/devspec:tasks` |
| `/devspec.implement` | `/devspec:implement` |
| `/devspec.review` | `/devspec:review` |
| `/devspec.diagram` | `/devspec:diagram` |

Gemini uses colon namespacing for project commands. Keep canonical dotted `/devspec.*` names in documentation and artifacts.

## Adapter Rules

- `GEMINI.md` imports `AGENTS.md` and adds only Gemini-specific guidance.
- Each TOML command is a thin wrapper around `devspec/adapters/command-registry.md`.
- Each TOML command names the matching Copilot prompt and agent files as the source of intent.
- Gemini CLI command arguments are passed through the native custom-command argument behavior.
- `/devspec.diagram` defaults to SVG output. `format=` may contain any non-duplicated `+` combination of `svg`, `html`, and `mermaid`. Example: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`.
- Do not use Gemini shell injection in devspec command wrappers; let the agent read files through normal tool access and approvals.

## Enterprise Safety

| Area | Guidance |
| --- | --- |
| Context hierarchy | Root `GEMINI.md` is the repository context file. Global `~/.gemini/GEMINI.md` may exist, but repository workflow rules should remain here. |
| Custom commands | Project commands live in `.gemini/commands/devspec/` and should be version-controlled with the framework. |
| Extensions | Gemini extensions can package prompts, MCP servers, and commands, but this repository ships project commands first for reviewability. |
| Enterprise configuration | Organization-wide Gemini CLI settings should enforce approved auth, tool access, and MCP policy outside prompt artifacts. |
| Sandboxing | Prefer sandboxing or command approval for validation and implementation workflows, especially outside trusted folders. |
| Telemetry | Use Gemini CLI telemetry only when configured by the environment; otherwise record token or telemetry data as unavailable. |
| Trusted folders | Treat repository trust as a prerequisite before allowing write or execute workflows. |
| Ignore rules | Use `.geminiignore` in consuming repositories when generated files, secrets, or large local folders need exclusion. |

## Known Gaps

- Gemini CLI custom commands use `/devspec:story` style names, not exact `/devspec.story` names.
- Copilot prompt files do not automatically register as Gemini commands.
- Exact permission, sandbox, and telemetry behavior depends on the user's Gemini CLI configuration.

## Validation

Run the new repository, existing repository, story, and cross-tool recovery flows in `devspec/adapters/validation-flows.md` with Gemini CLI before treating the adapter as enterprise-ready.
