# devspec.diagram

Create one evidence-backed diagram with duplicate checks and durable queue state.

Invocation: `/devspec.diagram runtime architecture format=svg motion=none|explain`

<workflow command="devspec.diagram">
  <purpose>Create one evidence-backed diagram with duplicate checks and durable queue state.</purpose>
  <protocols>
    <protocol ref="ask" queue="single-blocker" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for one targeted diagram in the current approved context. An explicit process-flow batch request may generate every queued, non-duplicate process-flow candidate; devspec.extract otherwise owns existing-system diagram discovery, candidate listing, and all-or-selected generation approval.</scope>
  <input>Diagram queue ID, subject, work item, explicit process-flow batch request, format request, or optional `motion=none|explain` in the current repository or an explicitly scoped multi-repository system.</input>
  <rules>
    <rule>Read only the evidence the requested subject needs, the one diagram-type pattern selected, and its matching family template. Do not load unrelated templates or explore beyond the subject's confirmed boundary.</rule>
    <rule>Select the diagram type from devspec/architecture/_template/diagram-types.md. Start each SVG from the matching family-specific template that catalogue names for the selected type, and never reduce a selected family to generic boxes and arrows.</rule>
    <rule>Create only evidence-backed, non-duplicate diagrams and persist queue or overview state for recovery.</rule>
    <rule>Diagram type, family template, and layout are selected from the evidence and the type catalogue, not asked.</rule>
    <rule>Record an evidence blocker in the caller's decision record, never in the queue, and leave the caller's saved stage unchanged. A directly requested diagram has no caller: run it at the foundation stage, record its blocker in devspec/foundation/decisions.md, and end at `none` instead of returning. Blocking sets the caller's run state to blocked and its next action to devspec.clarify, which resumes this diagram request through the caller's saved resume reference; the caller's stage and its own pending next action survive unchanged behind that pointer.</rule>
    <rule>When the blocker is recorded in a work-item decision record, stamp it with that work item's current scope revision so a later change request supersedes it with the rest of that revision's evidence.</rule>
    <rule>Accept a stable queued `DIA-###` ID or diagram subject, record subject, type, evidence, output format, duplicate-check result, status, and next action in the queue, and index completed output in the overview. On an explicit process-flow batch request, generate every queued non-duplicate process-flow candidate, validate each output, update each queue row independently, and leave the caller lifecycle state unchanged.</rule>
    <rule>Default to SVG with title and description and validate its XML. Write Mermaid or HTML only when explicitly requested, and when you do, record it from `devspec/architecture/_template/diagram.md` or `diagram.html` so its evidence, assumptions, and maintenance notes stay with the output.</rule>
    <rule>Default to `motion=none`. Treat an explicit request for an animated diagram without a motion value as `motion=explain`; reject unsupported motion values.</rule>
    <rule>For `motion=explain`, animate only an evidence-backed sequence, flow, or state transition and follow the opt-in motion guidance in diagram-types.md. Keep the complete meaning visible in the static final frame, provide a reduced-motion result with no information loss, and do not add decorative motion or imply unsupported behavior.</rule>
    <rule>Record animated SVG output in the queue's existing Output field as `svg; motion=explain`. When HTML is also requested, inline the same SVG so its motion and reduced-motion behavior remain intact.</rule>
    <rule>Preserve the template's standalone dark visual contract: 1600 by 900 canvas, subtle grid, framed surface, monospace typography, semantic role colors, connectors behind cards, short labels, and a legend only when its notation needs explanation. Replace every placeholder before completion and use no external assets, scripts, iframes, foreign objects, remote fonts, or unsupported diagram families.</rule>
    <rule>Anchor every connector to a shape edge at both ends, keep each arrowhead visible instead of hidden behind the shape it points at, and remove any shape the evidence leaves unconnected. Keep label backgrounds clear of boundary strokes, other labels, and neighboring shapes, and give every color on a shape a matching legend entry.</rule>
    <rule>Keep explanations in supporting Markdown rather than the graphic. Keep a flowchart to one primary concern and split an overloaded diagram at a confirmed responsibility boundary; use `sequence` for ordered interactions and the process-flow template for end-to-end operational behavior.</rule>
    <rule>For process flows, make the happy path visually obvious; distinguish start or end, manual, automated, integration, decision, exception, and artifact steps; label loop-backs; and draw exception paths as labeled dashed rose arrows that terminate or reconnect to a named step.</rule>
  </rules>
  <entry>One approved diagram subject in the caller's current scope, or one directly requested queued ID or subject in confirmed repository scope, with duplicate check and queue access; reject requests that would alter caller lifecycle state.</entry>
  <outputs>
    <artifact path="devspec/architecture/artifact-queue.md" />
    <artifact path="devspec/architecture/overview.md" />
    <artifact path="devspec/foundation/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="diagram-complete" stage="caller" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="caller" run="blocked" next="devspec.clarify" />
    <transition outcome="standalone-complete" stage="foundation" run="complete" next="none" />
    <transition outcome="standalone-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Validate the queued output, including finite animation and final-frame and reduced-motion completeness when motion is requested; index only completed diagrams, and leave the caller's saved stage unchanged.</closure>
</workflow>
