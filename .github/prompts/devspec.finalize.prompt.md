---
name: "devspec.finalize"
description: "Create or update the implementation-ready finalized brief for the current devspec work item and record it in finalize.md."
argument-hint: "Optional: add reviewer notes, constraints, or additive guidance for finalization"
agent: "devspec.finalize"
---

Create or update `devspec/work-items/<feature-name>/finalize.md` for the current work item.

Optional user input:
${input:finalizeInput:Optional: add reviewer notes, constraints, or additive guidance for finalization}

Requirements:
- Follow the [Work-Item Target Pattern](PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required upstream artifacts must exist before finalization.
- If blockers remain, mark the brief as `not ready`.
- Do not invent missing requirements.
- Apply the relevant readiness gates in `devspec/foundation/rules.md` for bugs and security vulnerabilities.
- For multi-repo work, follow the [Multi-Repo Validation Pattern](PATTERNS.md#multi-repo-validation-pattern) and record only the configuration status in `finalize.md`.
- For single-repo work, do not add multi-repo configuration status.
- Write or update `finalize.md` using `devspec/work-items/_template/finalize.md` as the section contract.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
