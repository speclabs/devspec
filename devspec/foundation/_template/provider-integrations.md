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

| Provider | Preferred inputs | Guardrail |
| --- | --- | --- |
| GitHub | Full issue URL, supported pull request URL, or `owner/repo#123` | Avoid bare numbers unless repository context is configured. |
| Jira | Full issue URL or issue key such as `ABC-123` | Reject malformed keys or keys outside configured project patterns. |
| Azure DevOps | Full work item URL | Accept numeric ids only when organization and project context are configured. |

## Resolution Order

| Order | Input path |
| --- | --- |
| 1 | Full provider URL |
| 2 | Provider-qualified identifier |
| 3 | Ambiguous identifier after user clarification |
| 4 | Manual intake when external resolution is unavailable and the user chooses to proceed |

## Failure Handling

| Condition | Action |
| --- | --- |
| Invalid input format | Stop and explain why it is invalid. |
| Ambiguous provider | Ask one clarification question to identify the provider. |
| Known provider cannot resolve item | Stop intake and classify the failure as not found, access denied, or integration unavailable when possible. |
| Integration unavailable | Offer manual intake as an explicit fallback. |
| Provider resolution succeeds | Show resolved details and require explicit user confirmation before creating or updating the work-item folder. |
| Unverified provider input | Do not create a normal resolved work item. |

## Resolved Item Confirmation

Show this minimum confirmation set when provider resolution succeeds:

| Field | Required |
| --- | --- |
| Provider | yes |
| Identifier | yes |
| Title | yes |
| Type | when available |
| Current external status | when available |
| Canonical link | yes |
| Short summary | yes |

Offer only these confirmation actions:

| Action | Result |
| --- | --- |
| Confirm and continue | Continue normal resolved intake. |
| Reject and retry input | Ask for a corrected source. |
| Switch to manual intake | Continue only with manual intake requirements. |
| Cancel | Stop intake. |
| Custom Answer | Route to clarification; do not create or update the work-item folder until resolved. |

## MCP Server Expectations

| Expectation | Notes |
| --- | --- |
| Lookup tools | Validate and fetch work items by URL or provider-specific identifier. |
| Returned data | Include title, description, status, labels or type, links, and relevant metadata. |
| Failure detail | Distinguish not found, unauthorized, malformed input, and transient provider failures. |
| Secret handling | Avoid exposing secrets or credentials in prompt artifacts. |

## Authentication Guidance

| Rule | Guidance |
| --- | --- |
| Configuration | Keep provider authentication outside prompt artifacts. |
| Privilege | Use least-privilege tokens or service identities. |
| Access mode | Prefer read-only access for intake and review unless write-back is required. |

## Story Intake Contract

| Topic | Requirement |
| --- | --- |
| Source resolution status | Record a value from `devspec/glossary.md#source-resolution-status-values` in `meta.md`. |
| Lookup attempt | Record provider and resolution notes. |
| Manual status | Use only when the user explicitly chooses to continue without external resolution. |
| Manual intake | Require external reference, manual description, and manual acceptance criteria. |
| Resolved items | Require explicit user confirmation after showing resolved details. |
| Blocked status | Use when input is invalid or required resolution failed. |
| Confirmation result | Record it in `meta.md` and record the shown summary in `story.md`. |

## Operational Notes

| Rule | Note |
| --- | --- |
| Single source | Keep provider-specific details here instead of duplicating them across prompt files. |
| Maintenance | Update this file when provider formats, supported tools, or fallback policy changes. |
