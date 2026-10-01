# devspec.techstack

Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints.

Invocation: `/devspec.techstack`

<workflow command="devspec.techstack">
  <purpose>Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Stack evidence, target stack, or delivery constraint.</input>
  <rules>
    <rule>Inspect manifests, lockfiles, runtime configuration, and CI before asking material questions.</rule>
    <rule>Record runtime, languages, frameworks, data stores, tooling, supported versions, and material constraints.</rule>
  </rules>
  <entry>Completed project context in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/tech-stack.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.codebase-structure" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record inspected evidence and one registered next command.</closure>
</workflow>
