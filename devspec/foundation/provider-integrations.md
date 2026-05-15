# Provider Integrations

## Purpose

- Define how external work-item providers are resolved during `devspec.story`.
- Keep provider-specific access behind MCP servers or equivalent integration tools.
- Preserve a safe fallback to manual intake when provider resolution is unavailable.

## Integration Model

- Keep the `story` workflow provider-agnostic.
- Use one MCP server per provider or one internal MCP server that wraps multiple providers.
- Prefer exact provider resolution over inference from ambiguous identifiers.

## Supported Providers

### GitHub

- Preferred inputs: full issue URL, full pull request URL when intentionally supported, or `owner/repo#123`.
- Avoid bare numbers unless repository context is explicitly configured.

### Jira

- Preferred inputs: full issue URL or issue key such as `ABC-123`.
- Reject malformed keys or keys outside the configured project patterns.

### Azure DevOps

- Preferred inputs: full work item URL.
- Numeric ids are acceptable only when organization and project context are already configured.

## Resolution Order

1. Full provider URL
2. Provider-qualified identifier
3. Ambiguous identifier only after user clarification
4. Manual intake when external resolution is unavailable but the user still wants to proceed

## Failure Handling

- If the input format is invalid, stop and tell the user why it is invalid.
- If the provider is ambiguous, ask exactly one clarification question to identify the provider.
- If the provider is known but the item cannot be resolved, stop intake and report whether the failure appears to be not found, access denied, or integration unavailable.
- If the integration is unavailable, offer manual intake as an explicit fallback instead of guessing.
- If provider resolution succeeds, show the resolved item details and require explicit user confirmation before creating or updating the work-item folder.
- Do not create a normal resolved work item from unverified provider input.

## MCP Server Expectations

- Expose tools that can validate and fetch work items by URL or provider-specific identifier.
- Return enough data for title, description, status, labels or type, links, and relevant metadata.
- Distinguish not found, unauthorized, malformed input, and transient provider failures.
- Avoid exposing secrets or credentials in prompt artifacts.

## Authentication Guidance

- Configure provider authentication outside the prompt artifacts.
- Use least-privilege tokens or service identities.
- Prefer read-only provider access for intake and review workflows unless write-back is explicitly required.

## Story Intake Contract

- Record the source resolution status in `meta.md` as `resolved`, `manual`, or `blocked`.
- Record the provider and resolution notes whenever provider lookup is attempted.
- Use `manual` only when the user explicitly chooses to continue without external resolution.
- Manual intake requires a user-provided external reference, manual description, and manual acceptance criteria.
- For resolved items, require explicit user confirmation after showing the resolved details.
- Use `blocked` when the input is invalid or resolution is required but failed.

## Operational Notes

- Keep provider-specific details here instead of duplicating them across prompt files.
- Update this file when provider formats, supported tools, or fallback policy changes.