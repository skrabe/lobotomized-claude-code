<!--
name: 'Skill: Artifact dashboard HTML template'
description: >-
  KPI/chart/breakdown dashboard artifact HTML body fragment served as a
  reference template by the Artifact skill.
ccVersion: 2.1.210
-->
<!-- Artifact-tool body fragment — no <!DOCTYPE>/<html>/<head>/<body> wrapper. See SKILL.md for slot guidance. -->
<title><!-- SLOT: TITLE — plain text, e.g. "Q2 Revenue Dashboard" -->Dashboard</title>
<style>
  :root {
    /* Default styling = CDS token values, hardcoded because published artifacts
       render outside the CDS scope (no --cds-* vars at runtime).
       --row-hover is deliberately NOT a named token (derived hover wash).
       Hardcoded copies drift if tokens.css regenerates — acceptable for a
       template default; restyling on top makes a refresh a trivial :root swap.
       Tune --accent toward the subject — prefer another token from the shipped
       palette so the page stays on-system, and change it in every scope that
       declares it (this block and both dark scopes below) or it snaps back in
       dark mode. */
    color-scheme: light;
    --bg: #f9f9f7;            /* cds-surface-0 */
    --surface: #fcfcfb;       /* cds-surface-1 */
    --ink: #0b0b0b;           /* cds-text-primary */
    --ink-muted: #52514e;     /* cds-text-secondary */
    --line: rgba(11, 11, 11, 0.1);  /* cds-border */
    --accent: #184f95;        /* cds-text-accent */
    --good: #006300;          /* cds-text-success */
    --bad: #8e2626;           /* cds-text-danger */
    --row-hover: rgba(11, 11, 11, 0.04);
    --radius: 6px;
    --gap: 20px;
    font-family: ui-sans-serif, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  /* Dark mode — the frame viewer's documented content contract: OS preference
     as the default, the viewer's explicit toggle (data-theme on this root)
     overriding it. Values are the same CDS tokens' dark-block resolutions. */
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --bg: #0d0d0d;            /* cds-surface-0 dark */
      --surface: #1a1a19;       /* cds-surface-1 dark */
      --ink: #ffffff;           /* cds-text-primary dark */
      --ink-muted: #c3c2b7;     /* cds-text-secondary dark */
      --line: rgba(255, 255, 255, 0.1);  /* cds-border dark */
      --accent: #6da7ec;        /* cds-text-accent dark */
      --good: #0ca30c;          /* cds-text-success dark → green-400 */
      --bad: #ec7e7e;           /* cds-text-danger dark → red-300 */
      --row-hover: rgba(255, 255, 255, 0.05);
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --bg: #0d0d0d;
    --surface: #1a1a19;
    --ink: #ffffff;
    --ink-muted: #c3c2b7;
    --line: rgba(255, 255, 255, 0.1);
    --accent: #6da7ec;
    --good: #0ca30c;
    --bad: #ec7e7e;
    --row-hover: rgba(255, 255, 255, 0.05);
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-size: 14px;
    line-height: 1.5;
  }
  .page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 32px var(--gap);
    display: grid;
    gap: var(--gap);
    grid-template-columns: repeat(12, 1fr);
  }
  header.top { grid-column: 1 / -1; display: flex; align-items: baseline; justify-content: space-between; }
  h1 { margin: 0; font-size: 24px; font-weight: 600; letter-spacing: -0.01em; }
  .subtitle { color: var(--ink-muted); font-size: 13px; }

  .card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 16px 18px;
  }
  .card h2 { margin: 0 0 4px; font-size: 13px; font-weight: 500; color: var(--ink-muted); text-transform: uppercase; letter-spacing: 0.04em; }

  .kpis { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--gap); }
  .kpi .value { font-size: 28px; font-weight: 600; font-variant-numeric: tabular-nums; margin: 2px 0; }
  .kpi .delta { font-size: 12px; font-weight: 500; display: inline-flex; align-items: center; gap: 4px; }
  .kpi .delta.up { color: var(--good); }
  .kpi .delta.down { color: var(--bad); }
  /* Valence overrides — color by whether the change is good when direction ≠ goodness
     (a latency/cost/error drop is an improvement). Must stay after .up/.down to win. */
  .kpi .delta.good { color: var(--good); }
  .kpi .delta.bad { color: var(--bad); }

  .chart-primary { grid-column: 1 / -1; }
  .chart-primary .plot { height: 280px; }

  .breakdown { grid-column: 1 / -1; }
  table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 10px 8px; border-bottom: 1px solid var(--line); }
  th { font-size: 12px; font-weight: 500; color: var(--ink-muted); text-transform: uppercase; letter-spacing: 0.03em; }
  td.num, th.num { text-align: right; }
  tbody tr:hover { background: var(--row-hover); }

  footer.note { grid-column: 1 / -1; color: var(--ink-muted); font-size: 12px; text-align: center; padding-top: 8px; }

  @media (max-width: 720px) {
    .page { padding: 20px 14px; }
    h1 { font-size: 20px; }
  }
</style>

<div class="page">

  <header class="top">
    <h1><!-- SLOT: TITLE -->Dashboard Title</h1>
    <span class="subtitle"><!-- SLOT: optional date range / scope text -->Last 30 days</span>
  </header>

  <!-- SLOT: KPI_TILES
       Emit 2–5 .kpi cards. Each tile = one headline number the user cares about most.
       The .delta span is optional. Pick the ▲/▼ glyph and "up"/"down" class by direction;
       when a decrease is the improvement (latency, cost, errors), also add "good" or "bad"
       so the color follows meaning — e.g. class "delta down good" for latency that fell. -->
  <section class="kpis">
    <div class="card kpi">
      <h2>Metric label</h2>
      <div class="value">0</div>
      <span class="delta up">▲ 0%</span>
    </div>
    <!-- repeat .card.kpi per metric -->
  </section>

  <section class="card chart-primary">
    <h2><!-- SLOT: chart title — name the finding, not the axes -->Trend</h2>
    <div class="plot" id="primary-chart"></div>
  </section>

  <section class="card breakdown">
    <h2><!-- SLOT: breakdown title -->Breakdown</h2>
    <table>
      <thead>
        <tr>
          <!-- SLOT: BREAKDOWN_ROWS — column headers. Add class="num" to right-align numeric cols. -->
          <th>Name</th><th class="num">Value</th><th class="num">Share</th>
        </tr>
      </thead>
      <tbody>
        <!-- SLOT: BREAKDOWN_ROWS — one <tr> per row -->
        <tr><td>—</td><td class="num">0</td><td class="num">0%</td></tr>
      </tbody>
    </table>
  </section>

  <footer class="note"><!-- SLOT: FOOTER_NOTE — data source, timestamp -->Generated —</footer>
</div>

<!-- SLOT: PRIMARY_CHART_SPEC
     Emit a compact JSON spec describing the chart. renderChart() below turns it into SVG.
     Spec shape:
       {
         "series": [ { "name": "Revenue", "color": "var(--accent)", "points": [[x,y], ...] } ],
         "x": { "label": "Week", "ticks": ["W1","W2",...] },
         "y": { "label": "USD", "min": 0, "max": 100 }
       }
     Notes on the knobs:
       - Optional "type": "line" (default) | "bar" | "donut". Bar and donut render via
         the chart runtime injected at publish time; the built-in fallback below only
         draws lines, so prefer "line" unless the data genuinely isn't a trend.
       - Multi-series specs get a legend drawn from each series' "name".
       - "x.label" / "y.label" are optional axis captions; omit them when the chart title
         and tick labels already carry the units.
       - "y.min" / "y.max" are optional and used exactly as given (no headroom added).
         Defaults: the axis floors at 0 and tops out 5% above the data max. Set them when
         a narrow range far from zero (e.g. 97–99% uptime) would flatten the line.
       - Provide exactly one "x.ticks" label per data point (the upgraded chart aligns
         labels to points by index; with a different count it falls back to raw x
         values as labels). Use evenly spaced x values — indices 0,1,2,... are fine.
       - For "donut": one series; each point is [label-index, value] with slice labels in
         "x.ticks"; optional "colors" array on the series for slice colors.
     The data-chart-runtime attribute is load-bearing — publish-time chart injection
     keys on it; keep it on this element exactly as written.
     In JSON string values here, write any literal "</" as "<\\/" — an unescaped
     "</script" inside a string would terminate this script element early.
     Replace the placeholder spec below with real data — published output must never
     contain these placeholder values. -->
<script type="application/json" id="primary-chart-spec" data-chart-runtime>
{
  "series": [
    { "name": "REPLACE ME — placeholder, not real data", "color": "var(--accent)", "points": [[0,0],[1,0],[2,0]] }
  ],
  "x": { "ticks": ["—","—","—"] },
  "y": {}
}
</script>

<script>
/* Fallback line-chart renderer: reads the JSON spec above and draws an SVG
   into #primary-chart. Deterministic — same spec, same pixels. It renders
   first at parse time; when the publish-time chart runtime is present it
   replaces this output (adding bar/donut support). For the standard
   time-series case, fill the SLOT above rather than editing this; extending it
   (new chart types, more panels) is fine when the dashboard calls for it — keep
   extensions deterministic too: same data, same pixels. */
(function renderChart() {
  const spec = JSON.parse(document.getElementById('primary-chart-spec').textContent);
  const el = document.getElementById('primary-chart');
  const W = el.clientWidth || 800, H = el.clientHeight || 280;

  const note = text => {
    const msg = document.createElement('div');
    msg.textContent = text;
    msg.style.cssText = 'color:var(--ink-muted);text-align:center;padding-top:120px;';
    el.appendChild(msg);
  };

  const series = (spec.series || []).filter(s => Array.isArray(s.points) && s.points.length);
  if (!series.length) {
    note('No data');
    return;
  }
  if (spec.type && spec.type !== 'line') {
    /* Bar/donut need the injected chart runtime; this fallback only draws
       lines. The runtime replaces this note when present. */
    note('Chart requires the published page’s chart runtime');
    return;
  }

  const xLabel = (spec.x || {}).label, yLabel = (spec.y || {}).label;
  const hasLegend = series.length > 1;
  /* Top gutter stacks: row 1 y-axis caption (16px), row 2 legend (18px). Bottom gutter
     gains 16px for the x-axis caption. Absent knobs cost nothing — a single-series spec
     with no labels lays out exactly as before. */
  const pad = {
    t: 10 + (yLabel ? 16 : 0) + (hasLegend ? 18 : 0),
    r: 10,
    b: 24 + (xLabel ? 16 : 0),
    l: 44
  };
  const iw = W - pad.l - pad.r, ih = H - pad.t - pad.b;

  const allPts = series.flatMap(s => s.points);
  const xs = allPts.map(p => p[0]), ys = allPts.map(p => p[1]);
  const xMin = Math.min(...xs), xMax = Math.max(...xs);
  const yMin = (spec.y && spec.y.min != null) ? spec.y.min : Math.min(0, ...ys);
  const yMax = (spec.y && spec.y.max != null) ? spec.y.max : Math.max(...ys) * 1.05;
  const sx = x => pad.l + (xMax === xMin ? iw/2 : (x - xMin) / (xMax - xMin) * iw);
  const sy = y => pad.t + ih - (yMax === yMin ? ih/2 : (y - yMin) / (yMax - yMin) * ih);

  const ns = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', \`0 0 \${W} \${H}\`);
  svg.setAttribute('width', '100%'); svg.setAttribute('height', '100%');

  /* Every label lands via textContent — model-filled strings must never be
     concatenated into markup. */
  const text = (x, y, str, anchor) => {
    const t = document.createElementNS(ns, 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.setAttribute('text-anchor', anchor); t.setAttribute('font-size', '11');
    t.setAttribute('fill', 'var(--ink-muted)');
    t.textContent = str;
    svg.appendChild(t);
  };

  if (yLabel) text(0, 12, yLabel, 'start');
  if (hasLegend) {
    let lx = pad.l;
    const ly = (yLabel ? 16 : 0) + 13;
    series.forEach(s => {
      const sw = document.createElementNS(ns, 'rect');
      sw.setAttribute('x', lx); sw.setAttribute('y', ly - 9);
      sw.setAttribute('width', 10); sw.setAttribute('height', 10);
      sw.setAttribute('rx', 2); sw.setAttribute('fill', s.color || 'var(--accent)');
      svg.appendChild(sw);
      const name = s.name || '';
      text(lx + 14, ly, name, 'start');
      lx += 14 + name.length * 6.5 + 18; /* width estimate keeps layout deterministic */
    });
  }

  /* Tick precision follows the tick step: sub-1 steps get decimals so 0–1 scales render
     0.26/0.53/… instead of 0/0/1/1; steps ≥ 1 keep whole-number ticks. With an explicit
     y.min + y.max, labels render the step exactly (≤2 decimals) so they match gridlines. */
  const step = (yMax - yMin) / 4;
  let dec = (step > 0 && step < 1) ? Math.min(6, Math.ceil(-Math.log10(step)) + 1) : 0;
  if (spec.y && spec.y.min != null && spec.y.max != null)
    for (dec = 0; dec < 2 && step * 10 ** dec !== Math.round(step * 10 ** dec); dec++);
  for (let i = 0; i <= 4; i++) {
    const yv = yMin + (yMax - yMin) * i / 4, yp = sy(yv);
    const ln = document.createElementNS(ns, 'line');
    ln.setAttribute('x1', pad.l); ln.setAttribute('x2', W - pad.r);
    ln.setAttribute('y1', yp); ln.setAttribute('y2', yp);
    ln.setAttribute('stroke', 'var(--line)'); ln.setAttribute('stroke-width', '1');
    svg.appendChild(ln);
    text(pad.l - 8, yp + 4, yv.toLocaleString(undefined, { maximumFractionDigits: dec }), 'end');
  }

  const tickY = H - (xLabel ? 22 : 6);
  ((spec.x || {}).ticks || []).forEach((t, i, arr) => {
    const xp = sx(xMin + (xMax - xMin) * i / Math.max(1, arr.length - 1));
    text(xp, tickY, t, 'middle');
  });
  if (xLabel) text(pad.l + iw / 2, H - 6, xLabel, 'middle');

  series.forEach(s => {
    const d = s.points.map((p, i) => (i ? 'L' : 'M') + sx(p[0]) + ',' + sy(p[1])).join(' ');
    const path = document.createElementNS(ns, 'path');
    path.setAttribute('d', d); path.setAttribute('fill', 'none');
    path.setAttribute('stroke', s.color || 'var(--accent)'); path.setAttribute('stroke-width', '2');
    path.setAttribute('stroke-linejoin', 'round');
    svg.appendChild(path);
    const last = s.points[s.points.length - 1];
    const dot = document.createElementNS(ns, 'circle');
    dot.setAttribute('cx', sx(last[0])); dot.setAttribute('cy', sy(last[1]));
    dot.setAttribute('r', '3.5'); dot.setAttribute('fill', s.color || 'var(--accent)');
    svg.appendChild(dot);
  });
  el.appendChild(svg);
})();
</script>
