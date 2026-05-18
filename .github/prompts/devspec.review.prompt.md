---
name: "devspec.review"
description: "Review the current implemented devspec work item, record findings in review.md, and decide whether the work is approved or needs changes."
argument-hint: "Optional: add review focus areas, risk notes, or reviewer guidance"
agent: "devspec.review"
---

Review the current work item and update `devspec/work-items/<feature-name>/review.md`.

Optional user input:
${input:reviewInput:Optional: add review focus areas, risk notes, or reviewer guidance}

Requirements:
- Follow the [Work-Item Target Pattern](PATTERNS.md#work-item-target-pattern).
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); `finalize.md` and `implement.md` must exist.
- Read `finalize.md`, `tasks.md` when present, `implement.md`, and relevant changed code context.
- Review for scope adherence, bugs, regressions, security risks, missing validation, and missing tests.
- Write or update `review.md` using `devspec/work-items/_template/review.md` as the section contract.
- If the work item is a bug or security vulnerability, apply the stricter review expectations from `devspec/foundation/rules.md`.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
