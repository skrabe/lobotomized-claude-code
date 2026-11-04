<!--
name: 'Tool result: REPL calls failed after script end (count)'
description: >-
  Warning in the REPL result that N tool calls still running at script end then
  failed; their errors are listed with the script's error.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALLS_FAILED_AFTER_SCRIPT_END_COUNT_VAR_0
  - TOOL_RESULT_REPL_CALLS_FAILED_AFTER_SCRIPT_END_COUNT_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALLS_FAILED_AFTER_SCRIPT_END_COUNT_VAR_0.length} tool call(s) were still running when the script ended, and then failed: ${TOOL_RESULT_REPL_CALLS_FAILED_AFTER_SCRIPT_END_COUNT_VAR_1(TOOL_RESULT_REPL_CALLS_FAILED_AFTER_SCRIPT_END_COUNT_VAR_0)}. Their errors are listed with the script's error, which they did not cause. Add 'await' next time.
