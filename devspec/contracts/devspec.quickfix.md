# devspec.quickfix

Implement and validate one localized, low-risk enhancement or bug fix.

Invocation: `/devspec.quickfix Fix Orders empty-state text`

<workflow command="devspec.quickfix">
  <purpose>Implement and validate one localized, low-risk enhancement or bug fix.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use only for one localized, low-risk change that needs no work item. Route anything outside that boundary to devspec.story before editing code.</scope>
  <input>One localized bug fix or small enhancement.</input>
  <rules>
    <rule>Select one primary scope: UI, internal API, function/job, library, configuration, tests, or a user-defined bounded scope.</rule>
    <rule>A user-defined scope is allowed only when it is documented as localized and low risk; otherwise route it to story before editing code.</rule>
    <rule>Create a QF record, implement, and run focused validation in the same command.</rule>
    <rule>Name the record `QF-&lt;number&gt;-&lt;slug&gt;.md`, matching `^QF-[0-9]{1,12}-[a-z0-9]+(-[a-z0-9]+)*$`. Never assign the number automatically: use a number the developer supplied explicitly in an unambiguous marked form such as `id:4471`, and otherwise ask one material question offering the date-based `YYMMDD` plus a two-digit sequence taken as the next value free in `devspec/quickfixes/` for that date as the recommended choice, alongside the next value above the highest existing quickfix number, with Custom Answer additional. Never infer a number from unmarked digits in prose, and reject a number an existing quickfix already uses.</rule>
    <rule>Route public API contracts, database schema or migration, authentication or security work, breaking changes, unrelated concerns, and unresolved risk to story and suggested refinement without editing code.</rule>
    <rule>When routing, carry the QF ID and its recorded request and evidence into the story request, and record the created work-item ID in the quickfix record so the routed record closes instead of waiting indefinitely.</rule>
  </rules>
  <entry>One documented localized low-risk request at triage with one primary scope; reject any request this command must route.</entry>
  <outputs>
    <artifact path="devspec/quickfixes/QF-&lt;number&gt;-&lt;slug&gt;.md" />
  </outputs>
  <transitions>
    <transition outcome="complete" stage="complete" run="complete" next="none" />
    <transition outcome="material-blocker" stage="triage" run="blocked" next="devspec.clarify" />
    <transition outcome="routed" stage="routed" run="active" next="devspec.story" />
  </transitions>
  <closure>Record the selected route, validation evidence, and terminal next action. Direct implementation is allowed only for the declared low-risk scope.</closure>
</workflow>
