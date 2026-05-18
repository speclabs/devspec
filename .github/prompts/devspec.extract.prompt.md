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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Accept one or more GitHub, Azure DevOps, or GitLab repository URLs, or one or more local repository folder paths.
- Support a single repo, a monorepo root, or multiple related repos.
- Accept repository URLs only. Reject issue, pull request, merge request, work item, wiki, release, and pipeline URLs.
- Resolve and validate each source before extraction. If any source is ambiguous, unsupported, inaccessible, or malformed, stop and ask the user to correct it.
- For local paths, confirm the path exists and appears to be a repository or monorepo root before proceeding.
- Extract evidence from repository layout, dependency manifests, CI/CD, infrastructure, docs, ADRs, contribution guides, CODEOWNERS, style guides, and runtime or configuration surfaces when available.
- Distinguish durable principles from repository-derived facts.
- Never finalize `devspec/constitution.md` from code inference alone. Present candidate principle changes and require explicit user confirmation before writing them.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) for confirmation and clarification, including constitution changes and conflicting coding-standard evidence.
- Separate directly observed facts, high-confidence inferences, and candidate guidance.
- For coding standards, record source links or paths, language/framework-specific rules, and short evidence-backed examples when available.
- Write or update `devspec/architecture/overview.md` and the relevant files under `devspec/foundation/` in place.
- Organize `tech-stack.md` by project or repo with Markdown tables that include project versions and verified current market versions when available.
- Preserve human-authored content when updating existing artifacts. Prefer generated sections or conservative in-place merges instead of full-file replacement.
- Do not create ADR files unless the user explicitly asks and the decision has clear supporting evidence.
- Resolve missing facts through the one-question-at-a-time flow instead of leaving unresolved items whenever practical.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
