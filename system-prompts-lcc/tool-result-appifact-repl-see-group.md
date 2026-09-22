<!--
name: 'Tool Result: AppifactRepl See Group'
description: >-
  Per-claude.see() group text in the AppifactRepl tool_result: optional drop
  notice, wrapped body, and image-data note.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_0
  - TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_1
  - TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_2
  - TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_3
-->
${TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_0.dropped>0?`[the last ${TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_0.dropped} characters of this claude.see() text were dropped: the first ${TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_1} are shown]
`:""}${TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_2(TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_0.body)}${TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_3(TOOL_RESULT_APPIFACT_REPL_SEE_GROUP_VAR_0.images.length)}
