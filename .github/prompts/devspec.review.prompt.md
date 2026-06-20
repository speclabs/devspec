---
name: "devspec.review"
description: "Review implemented work for regressions, scope drift, risks, and validation gaps."
argument-hint: "Optional: add review focus areas, risk notes, or changed files"
agent: "devspec.review"
---

Review the current work item and update `devspec/work-items/<work-item-folder>/review.md`.

Review correctness, finalized scope, security, validation coverage, and unnecessary implementation complexity. Use the [Minimum Necessary Implementation Pattern](PATTERNS.md#minimum-necessary-implementation-pattern) only to flag unnecessary dependencies, speculative abstractions, duplicated helper layers, oversized task outputs, or implementation not required by the finalized brief.

Apply the [Task Quality Gate Pattern](PATTERNS.md#task-quality-gate-pattern) when reviewing task completion and implementation evidence.

Optional user input:
${input:reviewInput:Optional: add review focus areas, risk notes, or changed files}
