# Diagram Types

Use the smallest diagram that makes a confirmed relationship easier to understand. SVG is the default; HTML is an optional presentation shell.

## Shared visual grammar

- Start from the matching family-specific SVG template in this directory; do not reduce a selected family to generic boxes and arrows.
- Use the template's 1600 by 900 dark canvas, subtle grid, framed surface, short eyebrow, title, and evidence-backed subtitle.
- Draw connectors behind cards. Use semantic role colors only to distinguish meaning, not decoration; keep boundaries and optional or exception paths visually distinct.
- Keep labels short; use supporting Markdown for details. Every SVG needs a title and description, complete replacement of template placeholders, and XML validation.
- Include a small legend only when color, line style, or notation is not self-evident. Do not use external assets, scripts, iframes, foreign objects, remote fonts, or remote images.

## Select by question

| Type | Use when the reader asks | Minimum evidence | Show |
|---|---|---|---|
| System architecture | What owns or connects to what across the system? | source roots, integration points | boundaries, components, integrations |
| Application landscape | Which applications exist and how do they relate? | application roots, ownership, interfaces | applications, responsibilities, interface links |
| Infrastructure topology | Where and on what does the system run? | deployment and infrastructure configuration | runtime, environments, providers, network or data dependencies |
| Domain model | What data concepts relate? | types/schema/contracts | entities, fields only when useful, cardinality |
| Journey map | What happens to an actor over time? | observed user/system flow | stages, actor actions, system touchpoints, outcome |
| Mind map | What belongs in this problem space? | scoped discovery | central concern, grouped branches, open risks |
| Process flow | What steps and gates decide the result? | command contract or observed process | steps, decisions, success and exception paths |
| Quadrant | How should options be compared? | stated axes and rationale | axes, four meanings, evidence-backed placement |
| Sequence | Who calls whom, and in what order? | call path/contracts | participants, ordered messages, returns when relevant |
| State lifecycle | Which states and transitions are allowed? | persisted state/transition rules | start, states, transition labels, terminal or exception states |
| Timeline | What depends on what, and when? | milestones/dependencies | phases, milestones, dependency or risk links |

## Template selection

| Diagram type | SVG template |
|---|---|
| System architecture | `architecture-diagram.svg` |
| Application landscape | `application-landscape-diagram.svg` |
| Infrastructure topology | `infrastructure-topology-diagram.svg` |
| Process flow | `process-flow-diagram.svg` |
| Sequence | `sequence-diagram.svg` |
| State lifecycle | `state-lifecycle-diagram.svg` |
| Domain model | `domain-model-diagram.svg` |
| Journey map | `journey-map-diagram.svg` |
| Timeline | `timeline-plan-diagram.svg` |
| Quadrant | `quadrant-analysis-diagram.svg` |
| Mind map | `mindmap-diagram.svg` |

## Guardrails

Do not infer entities, callers, timelines, ownership, user sentiment, or priorities. Record uncertain information in the work item or decisions file, not as a factual diagram label. Keep a flowchart to one primary concern; split a diagram that cannot remain readable instead of shrinking text or crossing unrelated flows.

The journey template ships a signal row. Keep it only when a measured or user-confirmed signal supports every point; delete the row and its legend entry otherwise, because an unmeasured curve is inferred sentiment.

Every connector must start on one shape edge and end on another. A line that begins or ends in open space, or whose arrowhead is hidden behind the shape it points at, states a relationship the diagram does not actually show. Keep label backgrounds clear of boundary strokes and other labels, and keep every colour that appears on a shape present in the legend.

## Opt-in motion

Use motion only for `motion=explain`, and only when an evidence-backed order or transition helps the reader understand the diagram. A plain request for an animated diagram selects this mode. Static SVG remains the default.

- Put related shapes and labels in `<g>` elements and apply deterministic CSS animation delays in the represented sequence.
- Use embedded CSS keyframes without scripts. Prefer `transform` and `opacity`; for connector drawing, set `pathLength="1"` and animate normalized `stroke-dashoffset`. Do not animate path geometry, points, filters, or layout attributes.
- Run the explanation once and leave the complete final frame visible. Repeat only when the request explicitly describes a repeating operational state.
- Keep labels, connectors, and state distinctions understandable without motion. Animation may reinforce meaning but must not carry it alone.
- Add a `prefers-reduced-motion: reduce` rule that disables animation and transitions and explicitly restores final opacity, transform, and stroke offset values.
- Validate XML, internal references, finite timing, the final frame, and the reduced-motion result. Use `diagram-motion-sample.svg` as the implementation pattern.

For every completed diagram: save the output, update artifact-queue.md, and index the link in overview.md.
