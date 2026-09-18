<!--
name: 'Tool Description: Artifact How To Load A Library'
description: >-
  Artifact page-contract section on pinning CDN UMD builds, blocked downloads,
  native mermaid, and browser storage.
ccVersion: 2.1.276
variables:
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_3
  - TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_4
-->
${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_0} The viewer's sandbox also blocks any download the page starts itself — \`<a download>\` links (data:/blob: hrefs included) and script-driven saves are inert for viewers — so never offer a file through a plain link. Artifacts render mermaid diagrams natively — markdown via \`\`\`mermaid fences, HTML via \`<pre class="mermaid">\` blocks — no library needed, don't load one.

**Browser storage**: \`localStorage\` (also \`sessionStorage\` and IndexedDB) works, but each artifact has its own origin and the data lives only in that viewer's browser — it survives republishes to the same URL and never reaches other viewers, other devices, or Claude. It can come back empty or the accessor can throw (a private window, cleared or blocked site data, previews or thumbnail capture), so wrap every read and write in try/catch and render the page correctly without it. Use it only for per-viewer conveniences (a remembered tab or filter, a collapsed section, an unsent draft), never for state that must persist reliably, be shared between viewers, or be read back by Claude — state like that belongs in a runtime capability when this user has one: load the \`${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_1}\` skill before writing the page.

**Size**: The rendered page must be ${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_2/1024/1024}MB or smaller, and embedded data: URIs count toward that.

${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_3}

${TOOL_DESCRIPTION_ARTIFACT_HOW_TO_LOAD_LIBRARY_VAR_4}

**Icon** (on every first publish): Pass one short generic word as \`icon\` (e.g. \`"chart"\`, \`"calendar"\`, \`"recipe"\`) for the artifact's browser-tab icon — a plain signifier for what the page is, never a product or brand name, and never an emoji or markup. It stays the **same** for the life of an artifact, so on a redeploy (the same file path this session, or \`url\`) omit \`icon\` and the artifact keeps the one it has; pass a different one only when the user asks.
