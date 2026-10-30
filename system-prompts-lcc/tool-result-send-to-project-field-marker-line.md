<!--
name: 'Send to Project: Proposal field marker-shaped line'
description: >-
  Validation reason that a proposal field must not contain a marker-shaped line
  or the reserved block marker words.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_FIELD_MARKER_LINE_VAR_0
-->
${TOOL_RESULT_SEND_TO_PROJECT_FIELD_MARKER_LINE_VAR_0} must not contain a marker-shaped line (a word fenced by runs of punctuation, like ----- X -----, or the words BEGIN/END LOCAL HISTORY / SETUP PROPOSAL / TOOLS USED / PROJECT INSTRUCTIONS)
