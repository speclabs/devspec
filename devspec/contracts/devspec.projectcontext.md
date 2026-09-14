# devspec.projectcontext

Capture product purpose, users, outcomes, and scope boundaries.

Invocation: `/devspec.projectcontext`

<workflow command="devspec.projectcontext">
  <purpose>Capture product purpose, users, outcomes, and scope boundaries.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Product context, a confirmed source, or an explicit durable-principle promotion or retirement.</input>
  <rules>
    <rule>Capture purpose, users, outcomes, boundaries, and delivery context only. When the developer explicitly promotes or retires a rare cross-work-item principle, update `devspec/constitution.md` with its stable `CP-###` ID, evidence, state, and append-only history; do not infer a promotion.</rule>
  </rules>
  <entry>New foundation chain with project context absent, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/project-context.md" />
    <artifact path="devspec/constitution.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.techstack" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record the foundation state and one registered next command.</closure>
</workflow>
