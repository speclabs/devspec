# GitHub Copilot Adapter

GitHub Copilot in VS Code is the native and reference adapter for `devspec`.

## Reference Files

| File group | Role |
| --- | --- |
| `.github/prompts/*.prompt.md` | Registers the user-invoked `/devspec.*` commands and command-level required input. |
| `.github/agents/*.agent.md` | Defines stage behavior, tools, model fallback, constraints, handoffs, and output format. |
| `.github/prompts/PATTERNS.md` | Defines shared workflow, recovery, output, discovery, recommendation, and artifact patterns. |
| `.github/skills/` | Optional reusable skills that travel with the repository. |

## Compatibility Note

Do not change Copilot prompt or agent intent to support another tool. Other adapters must wrap or translate the Copilot reference behavior and remain conformant with `devspec/adapters/command-registry.md`.

## Validation

Before an enterprise release, verify VS Code with Copilot Chat recognizes every registered `/devspec.*` command and run the flow checklists in `devspec/adapters/validation-flows.md`.
