<!--
name: 'Data: Auto-mode recon settings.local indirection-gate blocked'
description: >-
  Auto-mode recon report fragment noting .claude failed the indirection gate,
  injected into the auto-mode classifier context.
ccVersion: 2.1.207
-->
${"\n#### Project `.claude/settings.local.json` — autoMode keys (found content, NOT pre-approved config)"}
\`.claude\` itself failed the indirection gate (it is not a real directory — e.g. committed as a symlink), so whether a settings.local.json exists behind it was deliberately not probed. Tell the user; do not read, resolve, or rewrite anything under this path.
