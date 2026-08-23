<!--
name: 'Skill Reference: Data-viz Anti-patterns'
description: >-
  Data-viz skill reference file (references/anti-patterns.md) cataloguing chart
  anti-patterns to check output against before shipping
ccVersion: 2.1.210
-->
# Anti-patterns — what goes wrong

## Color & encoding

**❌ Dual-axis charts (two y-scales on one plot).**
✅ Do instead: two charts, small multiples, or index both series to a common base
(=100 at t0) on **one** axis.

**❌ Recolor-on-filter.** Assigning colors by current rank, so filtering out a series
repaints the survivors.
✅ Color follows the entity, not its row number. Survivors keep their hue.

**❌ Cycling / generating hues past 8.** A 9th categorical color, generated or reused.
✅ Fold the tail into "Other," facet into small multiples, or use composite encoding.

**❌ Eyeballing colorblind-safety.** "These look different enough."
✅ Run \`scripts/validate_palette.js\`. Adjacent ΔE ≥ 8 (OKLab ×100), or 6–8 WITH secondary encoding.

**❌ A value-ramp on nominal categories.** Coloring each bar darker-where-bigger
when the categories have no natural order (products, teams, endpoints).
✅ One series → one color (slot 1) for every bar. Ordered categories (funnel,
tiers, age bands) → the ordinal ramp, validated with \`--ordinal\`.

**❌ Rainbow / non-neighbor sequential.** A multi-hue ramp for magnitude.
✅ One hue, light→dark. (Analogous neighbors or semantic heat are the only multi-hue
sequential exceptions, always with a scale legend.)

**❌ A hue at the diverging midpoint, or two cool hues as the two poles.**
✅ Two hues that read as opposite + a neutral gray midpoint.

**❌ Status color used for a non-status series** (or a series color used for status).
✅ Status tokens only when the color *means* good/bad; categorical when it's identity.

## Form

**❌ Eight categorical hues when the story is one number.** The most common way a
chart misses its point.
✅ Emphasis (highlight one, gray the rest), or a stat tile / hero number.

**❌ A one-bar bar chart, or a 2-slice pie.**
✅ A stat tile. The number is the chart.

**❌ A donut/pie for comparing close values.**
✅ A bar, or the numbers. Part-to-whole at a glance only, ≤ 6 segments.

**❌ More than ~7 color classes carrying meaning.**
✅ A table, or table + chart. Past ~7 bins, adjacent classes blur.

## Marks & chrome

**❌ Thick saturated blocks, heavy gridlines, no breathing room.** Reads loud, even
childish, at scale.
✅ Thin marks, hairline recessive grid/axes, generous padding. Saturated fills are
for small marks and accents, never large blocks.

**❌ Dashed gridlines or axis rules.** Dashing adds visual noise and reads as
"projection" or "threshold" when it's just a grid.
✅ Gridlines and axes are solid hairlines, one shade off the surface.

**❌ A number on every data point.** A value beside every dot or segment is chaos and goes unread.
✅ A legend is always present for ≥ 2 series; direct-label *selectively* (the endpoint, the extreme, the one series that matters) and let the axis + tooltip carry the rest.

**❌ A border drawn around marks to separate them.**
✅ A 2px surface gap between fills (stacked segments and adjacent bars alike) and a 2px surface ring (on overlapping markers).

**❌ A label clipped by, or overflowing, a too-small bar or stacked segment** —
including \`overflow: hidden\` cropping the first/last characters of an in-segment label.
✅ Only render a label inside a mark when it fits with padding; otherwise move it
outside the bar end, or drop it to the tooltip/legend (the value stays in the table view).

**❌ A chart container whose fixed height excludes the x-axis band** — the plot
fits, the axis labels don't, so the card gets a tiny nested vertical scroll.
✅ Size the container to include the axis labels (plot height + x-axis band),
or let the container grow with its content instead of fixing a height.

**❌ A display or serif face on the hero figure.** It reads as off-brand decoration.
✅ The hero figure uses the same sans as everything else.

**❌ \`tabular-nums\` on a large standalone number.** Equal-width digits make \`121\`
look loose at display sizes.
✅ Proportional figures on hero and stat-tile values; \`tabular-nums\` only where
numbers align vertically (table rows, axis ticks).

**❌ Texture on by default, or as decoration.** Dense angled fields are a vestibular
risk and read as noise on value scales.
✅ Texture is opt-in (a11y setting, print, forced-colors), 45°/135° only, ordered on
value scales.

## Interaction & accessibility

**❌ A tooltip as the only way to read a value.**
✅ Tooltips enhance, never gate — every value is also reachable via direct labels or
the table view; keyboard focus shows the same as hover.

**❌ Pinpoint hover targets — an 8px scatter dot you must land on dead-center.**
✅ The hit area includes the 2px gap and meets a ~24px minimum; dense scatter uses a nearest-point / Voronoi layer.

**❌ Per-chart filters, or filters inside a chart card.**
✅ One filter row above everything it scopes; all charts re-render against the same slice.

**❌ Skeleton flash on refetch.**
✅ Hold the previous render at reduced opacity — no layout jump.

**❌ No table view / color-only encoding on a continuous scale.**
✅ Every chart has a table-view twin (the WCAG-clean equivalent).
