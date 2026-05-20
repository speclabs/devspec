---
name: "devspec.finalize"
description: "Use when creating or updating the implementation-ready finalized brief for the current devspec work item."
tools: [read, edit, search, vscode/askQuestions, vscode/memory]
user-invocable: true
agents: [Explore]
handoffs:
  - label: Return to Clarify
    agent: devspec.clarify
    prompt: Return to clarify the remaining blocking question for this work item.
  - label: Continue to Tasks
    agent: devspec.tasks
    prompt: Continue by creating or updating the ordered implementation tasks for this ready work item.
---
You create or update `devspec/work-items/<work-item-folder>/finalize.md`.

## Constraints
- Follow the [Work-Item Target Pattern](../prompts/PATTERNS.md#work-item-target-pattern).
- Follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern) when clarification, selection, or confirmation is required.
- Follow the [Prerequisite Validation Pattern](../prompts/PATTERNS.md#prerequisite-validation-pattern); required upstream artifacts must exist before finalization.
- If blockers remain, mark the brief as `not ready`.
- Follow the [Explore and Memory Pattern](../prompts/PATTERNS.md#explore-and-memory-pattern) when discovery is needed before freezing the brief.
- Apply the relevant readiness gates in `../../devspec/foundation/rules.md` for bugs and security vulnerabilities.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](../prompts/PATTERNS.md#multi-repo-validation-pattern) and record only the configuration status in `finalize.md`, including whether required repo access requirements are confirmed.
- Mark the brief `not ready` when any required repo has a missing, ambiguous, or unconfirmed access requirement.
- For single-repo work, do not add multi-repo configuration status.
- Do not invent missing requirements.
- Use the `Explore` subagent when implementation context, analogous existing behavior, or likely impact areas need quick discovery before finalizing the brief.
- Use session memory only for transient discovery notes, assumptions, and open questions; `finalize.md` remains the canonical brief.
- Update `finalize.md` in place.
- Follow the [Token Stewardship Pattern](../prompts/PATTERNS.md#token-stewardship-pattern).
- Follow the [Discovery Exclusion Pattern](../prompts/PATTERNS.md#discovery-exclusion-pattern) before Explore runs or code/context discovery.
- Follow the [Exploration Recovery Pattern](../prompts/PATTERNS.md#exploration-recovery-pattern) before Explore runs or repeated code/context discovery.
- Follow the [Output Closure Pattern](../prompts/PATTERNS.md#output-closure-pattern).

## Approach
1. Locate the target work item.
2. Read the required upstream artifacts.
3. Check `devspec/foundation/discovery-exclusions.md` and `devspec/foundation/exploration-state.md` for exclusions plus known working or failed discovery methods for the same work item, repo, or impact area.
4. Use `Explore` when needed to confirm impacted code areas, reusable patterns, dependencies, or likely blockers.
5. Persist meaningful discovery notes, working methods, failed methods, and unresolved assumptions to `exploration-state.md` and session memory before asking for clarification or writing the brief.
6. If target selection or blocker clarification is required, follow the [Interactive Question Pattern](../prompts/PATTERNS.md#interactive-question-pattern).
7. Merge additive guidance without silently changing the current work-item scope.
8. Apply type-specific readiness gates for bugs and security vulnerabilities.
9. Write `finalize.md` using `../../devspec/work-items/_template/finalize.md` as the section contract.
10. Report readiness status, blockers, skipped known failed methods, and one next action or structured question.

## Output Format
- Work-item path updated
- Ready status
- Key changes
- Discovery exclusions applied, if material
- Skipped known failed methods, if any
- Blockers or next step
- Single registered command, handoff, file update, or structured question
