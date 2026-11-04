<!--
name: 'Tool result: REPL calls not started at script end'
description: >-
  Warning in the REPL result that some tool calls had not started when the
  script ended and did not run; tells the model to add await.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALLS_NOT_STARTED_AT_SCRIPT_END_VAR_0
  - TOOL_RESULT_REPL_CALLS_NOT_STARTED_AT_SCRIPT_END_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALLS_NOT_STARTED_AT_SCRIPT_END_VAR_0.length} tool call(s) had not started when the script ended, and did not run: ${TOOL_RESULT_REPL_CALLS_NOT_STARTED_AT_SCRIPT_END_VAR_1(TOOL_RESULT_REPL_CALLS_NOT_STARTED_AT_SCRIPT_END_VAR_0)}. Add 'await'.
