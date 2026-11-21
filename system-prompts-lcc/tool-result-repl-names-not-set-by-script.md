<!--
name: 'Tool Result: REPL names not set by script'
description: >-
  REPL result note listing names the script did not set because they already had
  a value
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_0
  - TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_1
  - TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_2
-->
 Not set by this script: ${TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_0.slice(0,TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_1).join(", ")}${TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_2>0?` and ${TOOL_RESULT_REPL_NAMES_NOT_SET_BY_SCRIPT_VAR_2} more`:""} (a name that already had a value keeps it, unless this script has it in a \`let\` with no value).
