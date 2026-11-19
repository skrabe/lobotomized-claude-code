<!--
name: 'Tool Result: REPL calls still running, no result'
description: >-
  REPL result note listing tool calls still running with no result and telling
  Claude to check before repeating them
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_CALLS_RUNNING_NO_RESULT_VAR_0
  - TOOL_RESULT_REPL_CALLS_RUNNING_NO_RESULT_VAR_1
-->

Tool calls that were still running, and gave no result: ${TOOL_RESULT_REPL_CALLS_RUNNING_NO_RESULT_VAR_0(TOOL_RESULT_REPL_CALLS_RUNNING_NO_RESULT_VAR_1)}. They may have run in part or in full, or may still be running, so check before making them again.
