<!--
name: 'Tool Result: REPL script names kept local'
description: >-
  Warning that a script's own names matching helpers stayed in the script and
  later scripts get the helpers back
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_0
  - TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_1
-->
This script's own ${TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_0.map((TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_1)=>`\`${TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_1}\``).join(", ")} stayed in this script, because ${TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_0.length===1?"a helper has that name":"helpers have those names"} here. Later scripts get the ${TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_0.length===1?"helper":"helpers"} again, not this script's ${TOOL_RESULT_REPL_SCRIPT_NAMES_KEPT_LOCAL_VAR_0.length===1?"value":"values"}.
