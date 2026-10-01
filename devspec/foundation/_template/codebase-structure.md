# Codebase Structure

| Area | Ownership | Boundary | Integration points | Validation location | Evidence |
|---|---|---|---|---|---|

## Repositories

| Repository | Role | Local path | In current workspace | Access requirement | Evidence | Work guidance |
|---|---|---|---|---|---|---|

Use `devspec/glossary.md#repository-access-requirements` for the access value. Do not infer access from a repository path. For missing or ambiguous access, first collect the repository path as free text, then ask for one access requirement before relying on that repository.

## Repository Layouts

For every repository above, record a representative tree rooted at its confirmed local path. Include solution or manifest files, owned source and test roots, meaningful modules, configuration, and integration or migration locations. Exclude dependencies, caches, generated output, and secrets. Use **Observed** for extracted source evidence and **Developer-defined** for a later custom layout or change.

### Repository: &lt;name or role&gt;

- **Root:** `&lt;confirmed local path&gt;`
- **Origin:** Observed | Developer-defined
- **Evidence:** &lt;source location or developer request/approval&gt;

```text
&lt;confirmed local path&gt;/
|-- &lt;solution-or-manifest&gt;
|-- &lt;owned-source-root&gt;/
|   `-- &lt;meaningful-module&gt;/
|-- &lt;test-root&gt;/
`-- &lt;configuration-or-migration-location&gt;/
```
