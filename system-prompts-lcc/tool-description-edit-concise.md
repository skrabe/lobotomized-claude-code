<!--
name: 'Tool Description: Edit (concise)'
description: >-
  Concise (velvet) Edit tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — single exact string replacement, must-Read-first, uniqueness
  requirement, replace_all option
ccVersion: 2.1.285
variables:
  - TOOL_DESCRIPTION_EDIT_CONCISE_VAR_0
  - TOOL_DESCRIPTION_EDIT_CONCISE_VAR_1
-->
Performs exact string replacement in a file.

- You must ${TOOL_DESCRIPTION_EDIT_CONCISE_VAR_0} the file in this conversation before editing, or the call will fail.
- \`old_string\` must match the file exactly, including indentation, and be unique — the edit fails otherwise. Strip the Read line prefix (${TOOL_DESCRIPTION_EDIT_CONCISE_VAR_1?"line number + a single tab or `:`":"line number + tab"}) before matching.
- \`replace_all: true\` replaces every occurrence instead.
