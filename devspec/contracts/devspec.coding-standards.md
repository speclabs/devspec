# devspec.coding-standards

Capture concise, reusable coding conventions, followable examples, and anti-patterns from source evidence or developer-defined standards.

Invocation: `/devspec.coding-standards`

<workflow command="devspec.coding-standards">
  <purpose>Capture concise, reusable coding conventions, followable examples, and anti-patterns from source evidence or developer-defined standards.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Observed conventions, approved standards, or developer-defined custom standards with followable numbered examples or example updates.</input>
  <rules>
    <rule>Keep only conventions that change implementation or review behavior.</rule>
    <rule>For an observed convention, assign a stable `CS-###` ID, cite its local source evidence, and record concise fenced code or test snippets as linked `EX-###` entries under `## Standards Examples`. Record an anti-pattern when repository evidence supports one.</rule>
    <rule>Accept a custom standard explicitly supplied or approved by a developer even when no local source example exists. Mark it developer-defined rather than observed, record its approval or request as evidence, assign or retain a stable `CS-###` ID, and include a concise illustrative `EX-###` entry for future implementations. For a developer-defined example, identify its source as the developer directive and date.</rule>
    <rule>For an explicit targeted update, accept added, replaced, or retired standards examples without rerunning extraction. Preserve existing `CS-###` and `EX-###` IDs, create new IDs without renumbering historical entries, and reconcile each standard's linked example IDs and origin.</rule>
  </rules>
  <entry>Completed codebase structure in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/coding-standards.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.rules" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record each retained standard with its stable ID, origin, linked numbered examples, and an anti-pattern when applicable and register one next command.</closure>
</workflow>
