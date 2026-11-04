<!--
name: 'Tool result: REPL call failed after script end'
description: >-
  Per-call warning in the REPL result naming a tool call that was still running
  at script end and then failed, with its truncated error.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_FAILED_AFTER_SCRIPT_END_VAR_0
  - TOOL_RESULT_REPL_CALL_FAILED_AFTER_SCRIPT_END_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALL_FAILED_AFTER_SCRIPT_END_VAR_0.toolName} was still running when the script ended, and then failed. Add 'await' next time. Its error:
${TOOL_RESULT_REPL_CALL_FAILED_AFTER_SCRIPT_END_VAR_1(TOOL_RESULT_REPL_CALL_FAILED_AFTER_SCRIPT_END_VAR_0.error??"",2000)}
