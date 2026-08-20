<!--
name: 'Skill: artifact-design'
description: >-
  Bundled artifact-design skill — design fundamentals for Artifacts. Calibrate
  the treatment to what the request actually calls for (utilitarian
  doc/plan/memo vs. editorial landing page/app), apply the every-artifact
  fundamentals (precedence, type, neutrals, layout, AI-slop avoidance, clean
  build, copy, UI-vs-document), then run the editorial process only when the
  read says so — so output is intentional, polished, and never reads as a
  template.
ccVersion: 2.1.234
-->
---
name: artifact-design
description: Design guidance and fundamentals for Artifacts.
when_to_use: Load before writing any artifact, including Markdown ones — format is part of the design pass, never a speed shortcut.
---

Pitch every artifact's visual identity at the treatment the task actually calls for. Make deliberate choices about palette, typography, and layout specific to this subject; avoid templated designs. When the user pins a visual direction, follow it exactly — their words always win.

## Read the request first

Calibrate the treatment, not whether to design. A doc deserves the same craft as a landing page; what changes is the treatment it's delivered in. Format is part of this read — decided, not defaulted: a Markdown publish keeps its filename as its title and takes almost none of the craft below, so it fits only when the user asked for Markdown or the content is bound for a Markdown-native destination; never pick it to save time.

A utilitarian treatment — a plan, a memo, a demo — gets real typographic hierarchy, considered spacing, and a proper palette, but doesn't get over-designed: most pages don't need a flashy, gigantic hero, and flourishes stay tasteful and limited. When unsure: a well-composed page is never the wrong answer; an over-designed visual identity sometimes is. An editorial treatment — a landing page, a game, an app or tool they'll keep or share — earns the process below.

The fundamentals apply to everything. The editorial process runs only when the read above says so.

## Fundamentals for every artifact

**Honor what's already there.** Look for an existing design system first — CLAUDE.md, a tokens or theme file, existing component styles. When one exists, apply it; everything below fills gaps and never overrides. Precedence: the user's words > the project's existing system > your choices.

**Ground it in the subject.** If the subject isn't clear, pin it: one concrete subject, its audience, the page's single job. The subject's own world — its materials, instruments, vernacular — is where distinctive choices come from. Build with real content throughout, never lorem.

**Pair typefaces.** Typography carries the page even when the page isn't about typography. Google Fonts is the one font host the Artifact CSP admits — link it directly (`<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">`); any other face must be inlined as an `@font-face` data URI or it falls back silently. Declare a real fallback stack either way. Keep running text near 65 characters wide, set a type scale and stay on it, give headings `text-wrap: balance` and uppercase labels a touch of letter-spacing.

**Choose neutrals, don't default to them.** A pure mid-grey reads as unconsidered; a grey biased slightly toward the accent reads as chosen. Pure white and near-black are fine grounds when they suit the subject — the point is the neutral was picked, not inherited.

**Design both themes.** The page renders in the viewer's theme, and the viewer has three states, not two: an explicit choice stamps `data-theme="dark"` / `data-theme="light"` on the root element, and the default "system" setting stamps *nothing* — most viewers see the un-stamped document, where only `prefers-color-scheme` separates light from dark. Structure the CSS token-level for all three: the bare `:root` block defines the complete light palette (for a deliberately dark-first design, swap light and dark consistently through this whole pattern); `@media (prefers-color-scheme: dark)` redefines only the tokens, guarded as `:root:not([data-theme="light"])` so an explicit light choice beats a dark OS; `:root[data-theme="dark"]` redefines them again so the toggle also wins in the other direction. Style components through the tokens, never directly inside a media or `[data-theme]` block — a color whose only definition sits behind `[data-theme]` never applies in the un-stamped state, and the page renders one theme's text on the other theme's ground. Two more rules keep each theme resolving as a set: the artifact composites over a ground the viewer paints in *its* theme, so `body` must set an explicit `background` from a token — a transparent body silently borrows the host's ground; and every element that sets a color takes it from the same token set as the surface behind it, never a literal that only works in one theme. Before publishing, scan the stylesheet for any color declared only inside a media or `[data-theme]` block — that is the classic unreadable-artifact bug. Give the second theme the same care as the first — don't naively invert; keep contrast legible and the accent working on both grounds. A design that deliberately commits to one visual world (a neon arcade screen, a letterpress invitation) may stay single-theme — then skip the media query and stamps entirely but still paint the background and every color explicitly, so the page holds on either host ground; make it a choice, not an omission.

**Let layout do the spacing.** Lay out sibling groups with flex or grid and `gap`, not per-element margins that collapse or double. Wide content — tables, code, diagrams — gets `overflow-x: auto` on its own container so the page never scrolls sideways. Use `font-variant-numeric: tabular-nums` wherever digits line up in columns.

**Avoid AI-generated design.** It clusters around a few looks: warm cream (#F4F1EA) with a serif display and terracotta accent; near-black with a lone acid-green or vermilion pop; broadsheet hairline rules with dense columns; a purple-to-blue gradient hero on white; Inter or Space Grotesk as the "safe" face; emoji section markers; everything centered; `rounded-lg` everywhere; accent bar/rail on rounded cards. Where nothing is specified, don't spend your freedom on one of these defaults.

**Build cleanly.** Look at the render before declaring done — overlapping elements, cascade collisions, and silent font fallbacks hide in the gap between source and output. Close every non-void element, double-quote attributes, give keyboard focus a visible state, respect `prefers-reduced-motion`. For decorative graphics, reach for Canvas or WebGL over hand-authored SVG path data.

**CSS rules.** Watch selector specificities — it's easy to generate classes that cancel each other out (a type-based `.section` fighting an element-based `.cta` over padding/margins). Structure the cascade so it doesn't silently undo your spacing.

**Writing the copy.** Words are design material, not decoration. Write from the user's side of the screen — name things by what people recognize, not how the system is built (a person manages *notifications*, not *webhook config*). Active voice; a control says exactly what happens ("Publish", then a toast that says "Published"). Errors explain what went wrong and how to fix it — no apologies, no vagueness. Specific beats clever.

**Structure is information.** Numbering, eyebrows, dividers, and labels should encode something true about the content, not decorate it. Numbered markers (01 / 02 / 03) are right only when the content actually is a sequence — a real process or typed timeline where order carries information the reader needs. Question whether a structural device earns its place before adding it.

**When it's a UI, not a document.** A dashboard or tool is scanned and operated, not read top-to-bottom, so the craft shifts from typography to information design. Surface the summary before the detail; encode state in form as well as number — a pill, chip, or severity stripe — so what needs attention reads at a glance. Semantic color (good / warning / critical) is separate from the accent hue and doesn't count as your accent. Give sparklines and charts the same care as type: an area fill, a faint grid, an emphasized endpoint. What's interactive should look interactive.

<!-- dataviz-callout -->

## Process

Before writing code, sketch a compact token system:
- **Color**: the palette as 4–6 named hex values.
- **Type**: typefaces for 2+ roles — a characterful display face used with restraint, a complementary body face, and a utility face for captions or data if needed.
- **Layout**: the concept in one or two sentences.

Then build, deriving every color and type decision from the plan.

## When the request is editorial

Make opinionated calls, and take one real aesthetic risk where it serves the work.

Review the plan against the subject before building: if any part reads like the generic default you'd produce for any similar page, revise it and note what you changed. Only after confirming the plan's uniqueness, write the code, following the revised plan exactly.

- **The hero is a thesis** — open with the most characteristic thing in the subject's world (headline, image, live demo, interactive moment).
- **Typography carries the personality.** Pair display and body faces deliberately — not the families you'd reach for on any other project — with a clear type scale and intentional weights, widths, spacing. Make the type treatment itself memorable.
- **Motion is deliberate.** Decide where — and whether — animation serves the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. One orchestrated moment lands harder than scattered effects; extra animation reads as machine-generated.
- **Match complexity to the vision.** Maximalist needs elaborate execution; minimal needs precision in spacing, type, detail.
- **Spend your boldness in one place;** keep everything around it quiet. If the accent fights the ground, shift it toward analogous or drop saturation rather than replacing it.
