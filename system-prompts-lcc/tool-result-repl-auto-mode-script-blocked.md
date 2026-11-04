<!--
name: 'Tool result: REPL auto mode script blocked'
description: >-
  REPL result explaining that auto mode's classifier or escape monitor blocked
  the script and stopped it or its running calls
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_0
  - TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_1
  - TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_2
  - TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_3
  - TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_4
-->
${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_0==="monitor"?`The API's escape monitor blocked auto mode's check of this script${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_1>0?` and ${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_2}`:""}`:TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_1>0?`Auto mode's classifier judged this script together with ${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_2}, and blocked them`:"Auto mode's classifier blocked this script"}, ${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_3?"so auto mode stopped the calls this script left running":"so auto mode stopped this script after it had started"}. ${TOOL_RESULT_REPL_AUTO_MODE_SCRIPT_BLOCKED_VAR_4}
