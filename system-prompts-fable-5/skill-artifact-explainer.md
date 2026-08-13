<!--
name: 'Skill: artifact-explainer'
description: >-
  Bundled artifact-explainer skill — Create an explainer artifact — a
  step-by-step conceptual walkthrough that teaches how something works. Use when
  the user asks to explain a concept, walk through a process, show how X works,
  make a tutorial, or produce a teaching-oriented page with a clear progression.
  Keywords — explainer, how it works, walkthrough, tutorial, step by step,
  concept. Only for CREATING a new artifact; edits to an existing artifact
  modify its HTML directly.
ccVersion: 2.1.210
-->
---
name: artifact-explainer
description: Create an explainer artifact — a step-by-step conceptual walkthrough that teaches how something works. Use when the user asks to explain a concept, walk through a process, show how X works, make a tutorial, or produce a teaching-oriented page with a clear progression. Keywords — explainer, how it works, walkthrough, tutorial, step by step, concept. Only for CREATING a new artifact; edits to an existing artifact modify its HTML directly.
---

Teaching-oriented layout: a lede that states what the reader will learn, followed by numbered steps that each pair a short prose explanation with a visual — usually a diagram, sometimes a code block or annotated example — ending with a recap.

## How to use

1. Read \`template.html\` from this skill's base directory (listed above).
2. Copy it as your starting point. Replace each \`<!-- SLOT: ... -->\` marker with real content — the comment inside each slot describes what goes there. Each slot also carries placeholder text after the comment (sample headings, sample steps, sample sentences); replace that text too — removing the comment markers alone leaves the placeholders in the published page.
3. Self-check the filled HTML before publishing: no \`SLOT\` markers left, no placeholder text left.
4. Publish the filled HTML with the \`Artifact\` tool.

**Creation only.** When editing an existing explainer artifact, work with its current HTML directly — don't re-read or re-apply this template.

## Grounding and honesty

- If no target was given, ask which file, directory, PR, system, or concept to explain — one short question — and stop until the user answers.
- For code, read the target and its immediate dependencies, callers, callees, types, and relevant tests before drafting. Explain what the code actually does by tracing it, not what its names suggest.
- Surface open questions and missing evidence plainly. A brief honest gap is better than a guess; do not pad simple sections.

## PR walkthroughs

Ground a PR walkthrough in the diff, PR body, and commit messages. The finished page must answer all five questions, wherever their answers fit naturally:

1. What problem is the PR trying to solve?
2. Why is it a problem?
3. How does the PR solve it?
4. What alternatives were considered?
5. Why is the current approach better than those alternatives?

If the available evidence does not answer a question — most often 4 or 5 — say so instead of inventing an answer. Include a concise before/after when the change has an observable surface; group the diff by logical change rather than file; identify what deserves reviewer attention; and close the tour with context the diff alone does not show, including rejected approaches and intentionally deferred follow-ups when documented.

## Flavor

The template's body offers two structures — keep one, delete the other (and its wrapper):

- **Numbered steps** (default): a progression the reader follows start to finish. Use for concept explainers — how something works.
- **Sections**: a tour of a system, change, or architecture, where reading order is looser and code carries more weight. Use for PR walkthroughs, codebase tours, and design overviews. Open with one wide architecture or flow diagram when the subject has a structural story; within sections, the code snippet is usually the subject matter itself — add a diagram only where structure or flow genuinely needs one.

## Slots

| Slot | What to fill in |
| --- | --- |
| \`TITLE\` | What's being explained, phrased as the question the reader has — e.g. "How does a Bloom filter work?" The title appears in **two places**: the \`<title>\` tag near the top (it becomes the browser-tab title) and the \`<h1>\` in the header — fill both. |
| \`LEDE\` | Two or three sentences: what the reader will understand by the end, and why it matters. |
| \`STEPS\` | Steps flavor: one \`<li class="step">\` per concept or stage. Each step has a heading, 1–3 short paragraphs of prose, and a \`.visual\` block — usually an inline SVG diagram; sometimes a \`<pre>\` code example or an annotated snippet. Keep each step to one idea. A step may end with an optional \`<p class="callout">\` aside — a gotcha, an analogy, or a pointer onward. |
| \`SECTIONS\` | Sections flavor: 2–7 \`<section class="topic">\` blocks, cut at the material's joints — group related material rather than splitting mechanically. Each has an \`<h2>\`, short prose, and \`.visual\` blocks that are usually code snippets; optionally open the whole flavor with one wide architecture diagram. The \`callout\` aside works here too. |
| \`RECAP\` | A short bulleted list restating the core takeaways in the reader's new vocabulary. |

## Visuals

- In the steps flavor, default to a diagram — most steps should carry one. Reach for a \`<pre>\` code block or a small table alone only when the concept is genuinely symbolic (syntax, exact values, comparisons); when both help, pair a diagram with a short code example in the same step. (The sections flavor inverts this balance — see Flavor above.) Code belongs in \`<pre>\`, not as text inside an SVG.
- Give every SVG a fixed \`viewBox\` and no width/height attributes — the template scales it.
- Keep SVG text 14–16px, with generous padding around shapes and labels.
- Use a simple, consistent visual vocabulary: boxes for things, arrows for movement or causality, and the accent — \`var(--accent)\` in a \`style\` attribute (\`var()\` fails silently in bare SVG attributes) — only on what the current step focuses on. Keep it identical across steps.
- Color every diagram through the template's tokens, via \`style\` attributes — never a hardcoded hex, named color, or \`white\`/\`black\` anywhere in an SVG: \`var(--ink)\` for text and strokes, \`var(--ink-soft)\` for secondary labels, \`var(--accent)\` for emphasis, \`var(--card)\` (or \`none\`) for box interiors, \`var(--bg)\` where a shape must match the page. A fixed color breaks in one of the viewer's two themes.
- Give each SVG \`role="img"\` and an \`aria-label\` stating what it shows.

## Notes

- The template is a **body fragment** — no \`<!DOCTYPE>\`/\`<html>\`/\`<head>\`/\`<body>\` wrapper. The Artifact tool adds its own skeleton at publish time.
- Each step's \`.visual\` block is a free-form container: put whatever best illustrates that step (SVG, code, a small table). There is no bundled renderer — author the visual directly.
- Steps flavor: aim for 3–6 steps — fewer suggests the sections flavor or a report, more should be split.
- Tune \`--accent\` in the \`:root\` block toward the subject if a different hue reads better.
