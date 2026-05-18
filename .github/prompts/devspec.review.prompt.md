---
name: "devspec.review"
description: "Review the current implemented devspec work item, record findings in review.md, and decide whether the work is approved or needs changes."
argument-hint: "Optional: add review focus areas, risk notes, or reviewer guidance"
agent: "devspec.review"
---

Review the current work item and update `devspec/work-items/<feature-name>/review.md`.

Optional user input:
${input:reviewInput:Optional: add review focus areas, risk notes, or reviewer guidance}

Execution:
- Pass optional review guidance to `devspec.review`; the agent owns target selection, prerequisite validation, code/context review, findings, artifact updates, and handoff behavior.
