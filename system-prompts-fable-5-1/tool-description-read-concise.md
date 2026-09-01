<!--
name: 'Tool Description: Read (concise)'
description: >-
  Concise (velvet) Read tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — absolute path, default line cap, image/PDF/notebook handling, and
  the "do not re-read a just-edited file" note
ccVersion: 2.1.177
variables:
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_0
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_1
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_2
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_3
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_4
  - TOOL_DESCRIPTION_READ_CONCISE_VAR_5
-->
Reads a file from the local filesystem.

- \`file_path\` must be an absolute path.
- Reads up to ${TOOL_DESCRIPTION_READ_CONCISE_VAR_0} lines by default${TOOL_DESCRIPTION_READ_CONCISE_VAR_1}.
${TOOL_DESCRIPTION_READ_CONCISE_VAR_2}
${TOOL_DESCRIPTION_READ_CONCISE_VAR_3}
- Reads images (PNG, JPG, …) and presents them visually.${TOOL_DESCRIPTION_READ_CONCISE_VAR_4()?' Reads PDFs via the `pages` parameter (e.g. "1-5", max 20 pages/request; required for PDFs over 10 pages).':""} Reads Jupyter notebooks (.ipynb) as cells with outputs.
- Reading a directory, a missing file, or an empty file returns an error or system reminder rather than content.${TOOL_DESCRIPTION_READ_CONCISE_VAR_5}
