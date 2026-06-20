# Implementation Task Plan

Use this artifact for executable implementation checkpoints. Keep recovery in `Resume State`; keep all task details in `Implementation Tasks`.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | tasks |
| Current command | `/devspec.tasks` |
| Current agent | devspec.tasks |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.tasks` |
| Resume notes | |
| Updated | |

## Planning Basis

Sources: `finalize.md#implementation-brief`, `finalize.md#validation-plan`, `finalize.md#readiness-assessment`, `devspec/foundation/codebase-structure.md`, and `devspec/foundation/rules.md`.

## Task Quality Review

Use this gate before handing off. Record material blockers in `Resume State`.

| Check | Evidence or gap | Next action |
| --- | --- | --- |
| Scope and source coverage | <finalized-scope-and-source-refs-covered-or-gap> | <none-or-blocker-action> |
| Validation coverage | <validation-plan-refs-covered-or-gap> | <none-or-blocker-action> |
| Dependency order and granularity | <sequencing-and-checkpoint-sizing-summary-or-gap> | <none-or-blocker-action> |
| Blockers, ambiguity, and risk | <access-target-scope-risk-or-follow-up-gap> | <none-or-blocker-action> |

## Implementation Tasks

Use one row per executable checkpoint. Keep rows compact; put traceability in `Source refs`, repository lists in `devspec/foundation/codebase-structure.md`, and only executable proof in `Validation`.

| ID | Task | Source refs | Target repository | Target area or files | Required access | Depends on | Validation | Done when | Status | Attempt count | Last checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | <developer-action> | <AC-PI-RISK-VAL-refs> | <repository-name> | <path-module-or-area> | See `devspec/glossary.md#access-requirement-values` | <task-id-or-none> | <command-method-or-review-signal-and-expected-result> | <observable-completion-condition-and-evidence> | pending | 0 | |
