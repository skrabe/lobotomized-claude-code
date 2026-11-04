<!--
name: 'REPL: Call Cap Reached'
description: >-
  Error thrown when a REPL script hits its tool-call cap; no later call of the
  script is answered.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_CAP_REACHED_VAR_0
  - TOOL_RESULT_REPL_CALL_CAP_REACHED_VAR_1
-->
${TOOL_RESULT_REPL_CALL_CAP_REACHED_VAR_0}: this script has made ${TOOL_RESULT_REPL_CALL_CAP_REACHED_VAR_1.toLocaleString("en-US")} calls, its cap. The call was not made, and no later call of this script will be answered.
