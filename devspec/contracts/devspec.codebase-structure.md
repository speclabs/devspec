# devspec.codebase-structure

Capture or customize owned source roots, repository layouts, module boundaries, integrations, and repository access.

Invocation: `/devspec.codebase-structure`

<workflow command="devspec.codebase-structure">
  <purpose>Capture or customize owned source roots, repository layouts, module boundaries, integrations, and repository access.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Repository layout, work area, integration, multi-repository context, or developer-defined structure update.</input>
  <rules>
    <rule>Map owned source roots, boundaries, integration points, and validation locations.</rule>
    <rule>For each repository, maintain a readable `text` layout tree rooted at its recorded local path. Include solution or manifest files, owned roots, meaningful modules, configuration, and integration or migration locations; keep it representative rather than exhaustive and exclude dependencies, caches, generated output, and secrets.</rule>
    <rule>For an explicit targeted update, accept a developer-provided layout tree or structure change without rerunning extraction. Mark developer-defined additions or changes as such, retain observed evidence where it remains accurate, and reconcile the repository table, layout tree, and area map.</rule>
    <rule>Reconcile the repository table with the access requirements repo-access recorded; never infer access from a repository path.</rule>
  </rules>
  <entry>Completed technology stack in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/codebase-structure.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.coding-standards" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record repository access boundaries, representative layout trees, and one registered next command.</closure>
</workflow>
