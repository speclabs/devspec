---
name: "devspec.extract"
description: "Create or refresh devspec constitution, architecture, and foundation artifacts from one or more GitHub, Azure DevOps, or GitLab repository URLs, or from local repository folder paths."
argument-hint: "Paste one or more supported repo URLs or local repo folder paths"
agent: "devspec.extract"
---

Create or refresh `devspec/constitution.md`, `devspec/architecture/overview.md`, and the relevant `devspec/foundation/*.md` artifacts from supported repository sources.

Required user input:
${input:extractSources:Paste one or more supported repo URLs or local repo folder paths}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Accept one or more GitHub, Azure DevOps, or GitLab repository URLs, or one or more local repository folder paths.
- Support a single repo, a monorepo root, or multiple related repos.
- Accept repository URLs only. Reject issue, pull request, merge request, work item, wiki, release, and pipeline URLs.
- Resolve and validate each source before extraction. If any source is ambiguous, unsupported, inaccessible, or malformed, stop and ask the user to correct it.
- For local paths, confirm the path exists and appears to be a repository or monorepo root before proceeding.
- Extract evidence from repository layout, dependency manifests, CI/CD, infrastructure, docs, ADRs, contribution guides, CODEOWNERS, and runtime or configuration surfaces when available.
- Distinguish durable principles from repository-derived facts.
- Never finalize `devspec/constitution.md` from code inference alone. Present candidate principle changes and require explicit user confirmation before writing them.
- Ask exactly one confirmation question at a time whenever explicit confirmation is required.
- Use clickable multiple-choice options whenever reasonable.
- Always include a `Custom Answer` option for confirmation questions.
- Always recommend one option with a short justification.
- Wait for the user's answer before asking the next confirmation question.
- Do not ask all confirmations at once.
- For `devspec/foundation/project-context.md`, `devspec/foundation/coding-standards.md`, and `devspec/foundation/rules.md`, separate directly observed facts from inferred or candidate guidance.
- Write or update `devspec/architecture/overview.md` and the relevant files under `devspec/foundation/` in place.
- Preserve human-authored content when updating existing artifacts. Prefer generated sections or conservative in-place merges instead of full-file replacement.
- Do not create ADR files unless the user explicitly asks and the decision has clear supporting evidence.
- Capture open questions explicitly instead of guessing missing facts.
- End the response with a recommended next step or next prompt to run.
- Summarize the sources processed, files updated, evidence used, confidence levels, confirmation blockers, and the recommended next step or prompt to run.