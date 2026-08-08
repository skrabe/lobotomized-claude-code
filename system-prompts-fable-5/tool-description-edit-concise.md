<!--
name: 'Tool Description: Edit (concise)'
description: >-
  Concise (velvet) Edit tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — single exact string replacement, must-Read-first, uniqueness
  requirement, replace_all option
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_EDIT_CONCISE_VAR_0
  - TOOL_DESCRIPTION_EDIT_CONCISE_VAR_1
  - TOOL_DESCRIPTION_EDIT_CONCISE_VAR_2
-->
Performs exact string replacement in a file.
${TOOL_DESCRIPTION_EDIT_CONCISE_VAR_0?"":`
- You must ${TOOL_DESCRIPTION_EDIT_CONCISE_VAR_1} the file in this conversation before editing, or the call will fail.`}
- \`old_string\` must match the file exactly, including indentation, and be unique — the edit fails otherwise. Strip the Read line prefix (${TOOL_DESCRIPTION_EDIT_CONCISE_VAR_2}) before matching.
- \`replace_all: true\` replaces every occurrence instead.
