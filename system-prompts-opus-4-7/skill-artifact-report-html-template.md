<!--
name: 'Skill: Artifact report HTML template'
description: >-
  Model-facing template.html scaffold for the artifact-report skill (masthead,
  key takeaways, TOC, sections, appendix) that the model fills in to author a
  report artifact.
ccVersion: 2.1.206
-->
<!-- Artifact-tool body fragment — no <!DOCTYPE>/<html>/<head>/<body> wrapper. See SKILL.md for slot guidance. -->
<title><!-- SLOT: TITLE -->Report</title>
<style>
  :root {
    --cds-surface-0: #f9f9f7;            /* page canvas */
    --cds-surface-1: #fcfcfb;            /* in-flow card */
    --cds-text-primary: #0b0b0b;
    --cds-text-secondary: #52514e;
    --cds-text-muted: #898781;           /* captions only — below AA for body text in light mode */
    --cds-border: rgba(11, 11, 11, 0.1);
    --cds-border-strong: rgba(11, 11, 11, 0.2);  /* unused by default — for the restyle pass */
    --cds-text-accent: #184f95;
    --cds-radius: 8px;
    --cds-font-voice: "Anthropic Serif", ui-serif, Georgia, "Times New Roman", serif;
    --cds-font-sans: "Anthropic Sans", ui-sans-serif, -apple-system, sans-serif;
    --cds-font-mono: "Anthropic Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-family: var(--cds-font-voice);
  }
  :root[data-theme="dark"] {
    --cds-surface-0: #0d0d0d;            /* gray-890 */
    --cds-surface-1: #1a1a19;            /* gray-830 */
    --cds-text-primary: #ffffff;         /* neutral-900 → gray-0 */
    --cds-text-secondary: #c3c2b7;       /* dark block re-points: gray-200 */
    --cds-text-muted: #898781;           /* dark block re-points: gray-400 (clears AA in dark) */
    --cds-border: rgba(255, 255, 255, 0.1);
    --cds-border-strong: rgba(255, 255, 255, 0.2);
    --cds-text-accent: #6da7ec;          /* blue-300 */
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --cds-surface-0: #0d0d0d;
      --cds-surface-1: #1a1a19;
      --cds-text-primary: #ffffff;
      --cds-text-secondary: #c3c2b7;
      --cds-text-muted: #898781;
      --cds-border: rgba(255, 255, 255, 0.1);
      --cds-border-strong: rgba(255, 255, 255, 0.2);
      --cds-text-accent: #6da7ec;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--cds-surface-0);
    color: var(--cds-text-primary);
    font-size: 17px;
    line-height: 1.65;
  }
  .doc {
    max-width: 680px;
    margin: 0 auto;
    padding: 72px 24px 96px;
  }

  .masthead { margin-bottom: 48px; border-bottom: 1px solid var(--cds-border); padding-bottom: 32px; }
  .eyebrow { font-family: var(--cds-font-sans); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cds-text-secondary); margin: 0 0 12px; }
  h1 { font-size: 36px; line-height: 1.15; margin: 0 0 12px; font-weight: 600; letter-spacing: -0.01em; text-wrap: balance; }
  .subtitle { font-size: 18px; color: var(--cds-text-secondary); margin: 0; }

  .takeaways { margin: 0 0 40px; padding: 18px 22px 16px; background: var(--cds-surface-1); border: 1px solid var(--cds-border); border-left: 3px solid var(--cds-text-accent); border-radius: var(--cds-radius); }
  .takeaways-label { font-family: var(--cds-font-sans); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--cds-text-secondary); margin: 0 0 8px; }
  .takeaways ul { margin: 0; padding: 0 0 0 18px; }
  .takeaways li { margin: 5px 0; line-height: 1.5; }
  .takeaways li::marker { color: var(--cds-text-accent); }

  nav.toc { margin: 0 0 48px; font-family: var(--cds-font-sans); font-size: 14px; border-left: 2px solid var(--cds-border); padding-left: 20px; }
  nav.toc .toc-label { text-transform: uppercase; letter-spacing: 0.06em; color: var(--cds-text-secondary); font-size: 11px; margin-bottom: 10px; }
  nav.toc ol { margin: 0; padding: 0 0 0 22px; }
  nav.toc li { margin: 7px 0; padding-left: 4px; }
  nav.toc li::marker { color: var(--cds-text-accent); font-weight: 600; font-variant-numeric: tabular-nums; }
  nav.toc a { color: var(--cds-text-primary); text-decoration: none; }
  nav.toc a:hover { color: var(--cds-text-accent); }

  section { margin: 0 0 40px; }
  h2 { font-size: 24px; margin: 40px 0 12px; font-weight: 600; text-wrap: balance; }
  h3 { font-size: 19px; margin: 28px 0 8px; font-weight: 600; }
  p { margin: 0 0 16px; }
  a { color: var(--cds-text-accent); }

  blockquote { margin: 20px 0; padding: 4px 0 4px 20px; border-left: 3px solid var(--cds-text-accent); color: var(--cds-text-secondary); font-style: italic; }
  pre, code { font-family: var(--cds-font-mono); font-size: 14px; }
  pre { background: var(--cds-surface-1); border: 1px solid var(--cds-border); border-radius: var(--cds-radius); padding: 14px 16px; overflow-x: auto; line-height: 1.5; }
  table { width: 100%; border-collapse: collapse; margin: 20px 0; font-family: var(--cds-font-sans); font-size: 14px; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--cds-border); }
  th { font-weight: 600; color: var(--cds-text-secondary); font-size: 12px; text-transform: uppercase; letter-spacing: 0.04em; }
  figure { margin: 24px 0; }
  figcaption { font-family: var(--cds-font-sans); font-size: 13px; color: var(--cds-text-secondary); margin-top: 8px; }

  .appendix { border-top: 1px solid var(--cds-border); margin-top: 56px; padding-top: 32px; }
  .appendix h2 { font-size: 19px; color: var(--cds-text-secondary); }

  @media print {
    :root, :root[data-theme="dark"], :root:not([data-theme="light"]) {
      --cds-surface-0: #ffffff;
      --cds-surface-1: #fcfcfb;
      --cds-text-primary: #0b0b0b;
      --cds-text-secondary: #52514e;
      --cds-text-muted: #898781;
      --cds-border: rgba(11, 11, 11, 0.1);
      --cds-border-strong: rgba(11, 11, 11, 0.2);
      --cds-text-accent: #184f95;
    }
    body { font-size: 12pt; }
    .doc { max-width: none; padding: 0; }
    table, pre, figure, blockquote, .takeaways { break-inside: avoid; }
    thead { display: table-header-group; }
    h2, h3 { break-after: avoid; }
  }
</style>

<article class="doc">

  <header class="masthead">
    <p class="eyebrow"><!-- SLOT: optional eyebrow — doc type / date, e.g. "Analysis · June 2026" -->Report</p>
    <h1><!-- SLOT: TITLE -->Document Title</h1>
    <p class="subtitle"><!-- SLOT: SUBTITLE -->One-line summary of what this document establishes.</p>
  </header>

  <!-- SLOT: KEY_TAKEAWAYS (optional) -->
  <aside class="takeaways" aria-labelledby="takeaways-label">
    <p class="takeaways-label" id="takeaways-label">Key takeaways</p>
    <ul>
      <li>First takeaway.</li>
    </ul>
  </aside>

  <nav class="toc">
    <div class="toc-label">Contents</div>
    <ol>
      <!-- SLOT: TOC_ITEMS -->
      <li><a href="#s1">Section one</a></li>
    </ol>
  </nav>

  <!-- SLOT: SECTIONS -->
  <section id="s1">
    <h2>Section heading</h2>
    <p>Body paragraph.</p>
  </section>

  <!-- SLOT: APPENDIX (optional)
       Supporting material that would interrupt the main flow: raw data tables,
       methodology notes, glossary. -->
  <section class="appendix">
    <h2>Appendix</h2>
    <p>Supplementary detail.</p>
  </section>

</article>

<script>
  (() => {
    const list = document.querySelector('nav.toc ol')
    const heads = document.querySelectorAll('article.doc > section:not(.appendix) > h2')
    const sections = document.querySelectorAll('article.doc section:not(.appendix)')
    if (!list) return
    if (heads.length === 0 || heads.length < sections.length) {
      list.dataset.toc = heads.length === 0 ? 'static-no-heads' : 'static-partial-match'
      return
    }
    list.dataset.toc = 'rebuilt'
    list.textContent = ''
    heads.forEach((h, i) => {
      const sec = h.parentElement
      if (!sec.id) sec.id = 'auto-s' + (i + 1)
      const a = document.createElement('a')
      a.href = '#' + sec.id
      a.textContent = h.textContent
      const li = document.createElement('li')
      li.appendChild(a)
      list.appendChild(li)
    })
  })()
</script>
