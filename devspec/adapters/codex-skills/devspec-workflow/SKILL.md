---
name: devspec-workflow
description: Use when running any /devspec.* workflow from OpenAI Codex while preserving the canonical Copilot command and agent intent.
---

# Devspec Workflow

Use this optional Codex skill as a starter template for repeated `devspec` workflows.

Before acting:

1. Read `AGENTS.md`.
2. Read `devspec/adapters/command-registry.md` for the requested `/devspec.*` command.
3. Read the canonical `.github/prompts/*.prompt.md` and `.github/agents/*.agent.md` files named by the registry.
4. Follow `AGENTS.md` for recovery, no-intent-drift, structured question behavior, and platform limitation handling.

Do not assume Copilot prompt files register as Codex slash commands. Treat the command name as workflow intent unless the active Codex surface provides its own matching command mechanism.
