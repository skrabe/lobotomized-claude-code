<!--
name: 'Tool result: REPL calls finished after script end'
description: >-
  Warning in the REPL result that tool calls ran to their end after the script
  ended without results; tells the model not to repeat them.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0
  - TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0.length} tool call(s) were still running when the script ended. They ran to their end, but the script ended before their results came: ${TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_1(TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0)}. Do not make them again. Add 'await' next time.
