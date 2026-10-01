# devspec.rules

Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules.

Invocation: `/devspec.rules`

<workflow command="devspec.rules">
  <purpose>Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="security" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Hard engineering, compliance, security, delivery, or accessibility constraints.</input>
  <rules>
    <rule>Keep non-negotiable rules separate from ordinary coding conventions and link applicable active `CP-###` constitution principles rather than duplicating them.</rule>
    <rule>State enforcement or validation for each rule when known.</rule>
  </rules>
  <entry>Completed coding standards in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/rules.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-ready" stage="foundation" run="active" next="devspec.story" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record enforceable rules and one registered next command.</closure>
</workflow>
