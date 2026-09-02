<!--
name: 'Tool Description: Artifact How To Load A Library'
description: >-
  Artifact page-contract section on pinning CDN UMD builds, blocked downloads,
  native mermaid, and browser storage.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_3
-->
${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_0} The viewer's sandbox also blocks any download the page starts itself — \`<a download>\` links (data:/blob: hrefs included) and script-driven saves are inert for viewers — so never offer a file through a plain link. Artifacts render mermaid diagrams natively — markdown via \`\`\`mermaid fences, HTML via \`<pre class="mermaid">\` blocks — no library needed, don't load one.

**Browser storage**: \`localStorage\` works (so do \`sessionStorage\` and IndexedDB). Each artifact is served from its own origin, so what a page stores is private to that artifact, survives republishes to the same URL, and lives only in that viewer's browser — it never reaches other viewers, the viewer's other devices, or Claude. It can come back empty (a private window, cleared site data, a different browser), and in some contexts the accessor itself throws (thumbnail capture, previews, browsers set to block site data) — so wrap every read and write in try/catch and render the page correctly with no stored value. It is not the place for anything that must persist reliably, be shared between viewers, or be read back later by Claude.

**Size**: The rendered page must be ${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_1/1024/1024}MB or smaller, and embedded data: URIs count toward that.

${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_2}

${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_3}

**Favicon** (required on a first publish): Pass one or two emoji as \`favicon\` (e.g. \`"📊"\`, \`"🐛"\`, \`"⚡🔥"\`). It becomes the browser-tab icon. Emoji only — no SVG, no markup. It stays the **same** for the life of an artifact — users find their tab by its icon, and a changed favicon reads as a different page — so on a redeploy (the same file path this session, or \`url\`) omit \`favicon\` and the artifact keeps the icon it has; pass a different one only when the user asks for a new icon.
