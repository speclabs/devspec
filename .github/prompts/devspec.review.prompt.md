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
- Use the current work-item context if it is clear. Otherwise, ask the user to select the target work item.
- Fail fast with guidance if `finalize.md` or `implement.md` is missing.
- Treat optional user input as additive only.
- Read `finalize.md`, `tasks.md` when present, `implement.md`, and relevant changed code context.
- Review for scope adherence, bugs, regressions, security risks, missing validation, and missing tests.
- Write or update `review.md` with review status, findings by severity, validation gaps, type-specific review notes, and next step.
- If the work item is a bug or security vulnerability, apply the stricter review expectations from `devspec/foundation/rules.md`.
- End the response with a recommended next step or next prompt to run.
- Summarize the work-item path updated, review status, top findings, next step, and the recommended next step or prompt to run.