---
name: devspec-changerequest
description: Run /devspec.changerequest using the canonical devspec command registry. Records one missed related requirement for a finalized work item without rewriting baseline history.
---

Execute canonical command `/devspec.changerequest`.

1. Read `AGENTS.md` for canonical workflow, no-intent-drift, cross-tool recovery, and structured question rules.
2. Read `devspec/adapters/command-registry.md` for this command's required input, outputs, mutation level, and next handoff.
3. Read `.github/prompts/devspec.changerequest.prompt.md` and `.github/agents/devspec.changerequest.agent.md` as the authoritative source of command intent and behavior.
4. Apply `.github/prompts/PATTERNS.md` for shared behavior: interactive questions, prerequisite validation, session recovery, and output closure.
5. Preserve baseline rows and prior evidence; append accepted `CR-###` scope only to existing work-item artifacts.

Command input comes from the user's current message.
