# Enterprise Operating Guide

Use this guide when adopting `devspec` across teams, repositories, or AI coding tools.

## Governance Controls

| Area | Requirement |
| --- | --- |
| Model allowlist | Record approved models or model families per adapter. Do not require adapter files to name a model that the target platform cannot enforce. |
| Tool permissions | Define which adapters may read, edit, execute commands, use browsers, call MCP tools, or access external systems. |
| Repository access | Use `devspec/foundation/codebase-structure.md` as the source of truth for `reference-only`, `edit`, `edit-and-test`, `validation-only`, `release-coordination`, and `unavailable` access. |
| Secrets | Keep tokens, API keys, provider credentials, and local secrets outside prompt, agent, adapter, and artifact files. |
| Provider access | Use `devspec/foundation/provider-integrations.md` for supported providers, accepted formats, lookup behavior, manual fallback, and access expectations. |
| Audit evidence | Store decisions, readiness, tasks, implementation checkpoints, validation, and review outcomes in Git-tracked `devspec` artifacts. |
| Security work | Follow security-vulnerability handling rules from `devspec/foundation/rules.md` and avoid recording unsafe exploit detail unless explicitly approved. |
| Human approval | Require explicit confirmation where the canonical prompt or agent contract requires it, especially provider resolution, repository access, constitution changes, and continuation after blockers. |
| Gemini CLI posture | Use trusted folders, sandboxing, `.geminiignore`, enterprise settings, and telemetry policy where available; keep Gemini extensions and MCP configuration outside prompt artifacts unless intentionally packaged. |
| Antigravity posture | Prefer strict mode or request-review settings for terminal commands, browser actions, MCP calls, non-workspace file access, and artifact application; keep projects scoped to recorded repositories. |

## Enterprise Rollout Gates

| Gate | Required evidence |
| --- | --- |
| Copilot baseline confirmed | Existing `.github/prompts` and `.github/agents` files remain unchanged in intent and still register the expected workflow in VS Code. |
| Adapter conformance confirmed | Each adapter maps to `devspec/adapters/command-registry.md` and records platform gaps in `devspec/adapters/compatibility-matrix.md`. |
| New repository flow passed | The new repository flow in `devspec/adapters/validation-flows.md` passes for the adapter. |
| Existing repository flow passed | The existing repository flow in `devspec/adapters/validation-flows.md` passes for the adapter. |
| Story flow passed | One feature, bug, or security work item completes intake through review. |
| Cross-tool recovery passed | A flow paused in one adapter resumes in another using only Git-tracked artifacts. |

## Operating Principles

- Keep the repository, not the AI session, as the durable source of truth.
- Prefer small, reviewable adapter changes over broad prompt rewrites.
- Add new adapters by mapping to the registry first, then validating with flow checklists.
- Treat compliance, security, production access, and external provider writes as explicit governance decisions.
