<!--
name: 'Skill Reference: Data-viz Reference Palette'
description: >-
  data-visualization reference (references/palette.md) the skill tells the model
  to Read.
ccVersion: 2.1.332
-->
# Reference palette

This is the **reference instance** of the data-viz method: every parameter the
method needs, filled in with a validated default palette. The rest of the skill
is system-agnostic - **to target your brand, substitute this file's values** and
re-run the validator. Nothing else changes.

## How to use these values

Everything below is plain hex. In an HTML chart, **define the slots you use as
CSS custom properties in a local \`<style>\` block** at the top of the file, then
reference them by role throughout - so the light/dark values swap in one place,
and the chart body is written against roles rather than raw hex:

\`\`\`css
.viz-root {
  color-scheme: light;
  --surface-1:      #ffffff;   /* chart surface */
  --text-primary:   #191919;
  --text-secondary: #666666;
  --series-1:       #257de0;   /* categorical slot 1 */
  /* ...only the roles this chart uses */
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) .viz-root {
    color-scheme: dark;
    --surface-1:      #191919;
    --text-primary:   #efefef;
    --text-secondary: #9c9c9c;
    --series-1:       #338ced;
  }
}
:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface-1:      #191919;
  --text-primary:   #efefef;
  --text-secondary: #9c9c9c;
  --series-1:       #338ced;
}
\`\`\`

Declare the dark values under both scopes as above - the media query covers
the OS setting; the \`data-theme\` scope covers the viewer's theme toggle,
which must win both ways (the \`:not(...)\` guard lets a light stamp beat
OS-dark; \`:where()\` keeps the media block below the toggle scope).

## Categorical palette

Both modes are selected. The dark column is the same eight hues stepped for the
dark surface, not a separate palette:

| Slot | Hue | Light | Dark |
|------|-----|-------|------|
| 1 | blue | \`#257de0\` | \`#338ced\` |
| 2 | orange | \`#f47230\` | \`#e76624\` |
| 3 | aqua | \`#00b894\` | \`#00a888\` |
| 4 | yellow | \`#f2a600\` | \`#d28e05\` |
| 5 | magenta | \`#ee7fac\` | \`#e24d8b\` |
| 6 | green | \`#008a17\` | \`#0aac23\` |
| 7 | violet | \`#6a4ce2\` | \`#9887ef\` |
| 8 | red | \`#ec4647\` | \`#eb6263\` |

This order passes every hard gate in both modes on the default *adjacent*
pairlist (stacks, bars, lines): worst adjacent CVD Delta E 11.8 light / 10.1 dark
(OKLab ×100, >=8 target), worst adjacent normal-vision Delta E 20.5 light / 21.1
dark (>=15 floor). Under \`--pairs all\` (scatter, bubble, choropleth, small
multiples) the full eight cannot clear the floors - with all 28 pairs in
play no ordering can (the pairlist no longer depends on order), and
re-stepping is off the table by the documented-palette rule - so those
chart forms carry a series cap: **the first three slots validate all-pairs
in both modes** (worst pair CVD Delta E 12.6 light / 12.8 dark, normal-vision 23.0
light / 19.4 dark - clear of the CVD warn band). Past three, fold to "Other" or
facet: the fourth slot puts yellow and orange on screen
together, and that pair fails the all-pairs floors (normal-vision 12.4
light / 9.8 dark; CVD 3.5 dark). No four of the eight hues pass all-pairs in
both modes, so re-ordering cannot raise the cap. Four light-mode slots (orange,
aqua, yellow, magenta) sit below 3:1 contrast on the light surface: the
**relief rule** applies (ship visible direct labels or the table view). The dark
steps sit in the dark band (OKLCH L ~ 0.48-0.70), clear 3:1 on the dark surface,
and validate as a set. When you swap in your own ramps, hold your palette to the
full gate.

The slot **ordering** is the CVD-safety mechanism, not cosmetic - candidate
orderings were enumerated and only those clearing every adjacent gate in both
modes kept (see \`color-formula.md\` § Themes); this default is one of the
passing orders, picked among them for its opening colors. When you swap in
your brand's hues, do the same: run the validator on candidate orderings and
choose only among the passing ones.

## Sequential hue

Default single hue: **blue**, light->dark. When two sequential contexts appear at
once, the second takes the next categorical slot's hue (orange), each as its own
one-hue ramp.

| step | hex | step | hex | step | hex | step | hex |
|---|---|---|---|---|---|---|---|
| 100 | \`#cce3fd\` | 250 | \`#84b9f3\` | 400 | \`#338ced\` | 550 | \`#1b64be\` |
| 150 | \`#b6d5f8\` | 300 | \`#6aabf1\` | 450 | \`#257de0\` | 600 | \`#1757ac\` |
| 200 | \`#9dc8f7\` | 350 | \`#519ced\` | 500 | \`#2370cd\` | 650 | \`#0f4a96\` |
| | | | | | | 700 | \`#0e3d7e\` |

The full 100->700 range is for **sequential** encoding (continuous magnitude -
heatmaps, choropleths) where the lightest step means "near zero" and is allowed
to recede toward the surface. For an **ordinal** ramp (discrete ordered marks -
funnel stages, tiers - validated with \`--ordinal\`), the step nearest the surface
must still clear 2:1: on light, start no lighter than **step 250** (\`#84b9f3\`,
2.06:1); on dark, go no darker than **step 600** (\`#1757ac\`, 2.51:1; step 650
only just clears it, at 2.04:1).

## Diverging pair

**blue <-> red** - warm/cool poles that read as opposite. Neutral midpoint is gray
(light \`#efefef\`, dark \`#383838\`). Equal step count per arm. (blue<->aqua was
rejected - both cool, the midpoint doesn't read as "nothing".)

## Status palette (fixed - never themed)

| role | hex | light-surface contrast | dark-surface contrast |
|---|---|---|---|
| good | \`#0aac23\` | 3.03 | 5.81 |
| warning | \`#fbb315\` | 1.82 | 9.68 |
| serious | \`#f18a59\` | 2.46 | 7.13 |
| critical | \`#dc3c3d\` | 4.41 | 3.98 |

Dark: same four steps - all clear 3:1 on the dark surface (\`#191919\`), and good
is the same green as dark slot 6. On the light surface, warning and
serious are sub-3:1 by design; the **icon + label** pairing is the mitigation, so
a status color never carries meaning alone. That green aside, these steps are
deliberately distinct from the categorical slots so a status color never
impersonates a series -
distinct enough that nothing collides at a glance, not enough for hue to
carry the distinction unaided: measured by the series floor's own bar
(unsimulated Delta E >= 15), nine categorical-vs-status pairs per mode sit
below 15 - in light mode yellow vs warning measures 3.6, red vs critical 3.8,
slot-2 orange sits 5.2 from status-serious, and the success text
green \`#006c10\` sits 9.3 from the series green; green vs status-good is 10.1
in light mode, and the two are identical in dark. The rule is general: any series color beside a
same-hue-family status or delta cue leans on the icon + label pairing and on
placement; never on hue alone.

## Texture fill (the accessibility channel)

One hand-drawn **"Lines"** fill, used at **45° and its 135° mirror only**. Inked
tone-on-tone (a darker step of the fill's own ramp). On value scales it is
*ordered* (rotation steps with magnitude; arm angle carries the diverging sign).
Triggered by the accessibility setting, print, or \`forced-colors\` - never
decorative, never on by default.

## Surfaces (for the validator)

- Light chart surface: \`#ffffff\`
- Dark chart surface: \`#191919\`

These are the validator's built-in defaults. **When you swap in your own
palette, re-run against your own surfaces:**
\`--surface <your-light> --mode light\` and \`--surface <your-dark> --mode dark\` -
contrast and band results are only meaningful against the surface the chart
actually renders on.

## Chart chrome & ink

| Role | Light | Dark |
|---|---|---|
| Chart surface | \`#ffffff\` | \`#191919\` |
| Page plane | \`#f9f9f9\` | \`#0b0b0b\` |
| Primary ink | \`#191919\` | \`#efefef\` |
| Secondary ink (axis ticks and titles, legend, subtitle) | \`#666666\` | \`#9c9c9c\` |
| Label inside a categorical or status fill | \`#ffffff\`, except \`#0b0b0b\` on yellow and warning | \`#ffffff\`, except \`#0b0b0b\` on warning |
| Gridline (hairline) | \`#e7e7e7\` | \`#303030\` |
| Baseline / axis | \`#c2c2c2\` | \`#474747\` |
| Delta up good (success text) | \`#006c10\` | \`#53c556\` |
| Border (hairline ring) | \`rgba(11,11,11,0.10)\` | \`rgba(255,255,255,0.10)\` |

## Filter controls

Filters are standard UI, not chart components - the chart layer only adds the
composition rules in \`interaction.md\`. A date-range control is a list of preset
rows (today, last 7/30/90 days, month-to-date) with selection marked by a 16px
bold check, hover as a ghost wash, and custom range behind a hairline in the
footer. Dimension filters are a standard combobox.

## Typeface & figures

Everything - including the hero figure - stays in the system sans: \`system-ui,
-apple-system, "Segoe UI", sans-serif\`. No display or serif face anywhere. Large
standalone numbers (hero figure, stat-tile values) use the default proportional
figures; reserve \`font-variant-numeric: tabular-nums\` for columns that must align
vertically (table rows, axis ticks). Substitute your brand's UI sans here.
