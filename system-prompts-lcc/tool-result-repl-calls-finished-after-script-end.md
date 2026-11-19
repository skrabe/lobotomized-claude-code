<!--
name: 'Tool Result: REPL calls finished after script end'
description: >-
  REPL warning that tool calls were still running at script end and finished or
  moved to background; don't repeat them
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0
  - TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0.length} tool call(s) were still running when the script ended. They have since finished or moved to the background, where they may still be running, but the script ended before their results came: ${TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_1(TOOL_RESULT_REPL_CALLS_FINISHED_AFTER_SCRIPT_END_VAR_0)}. Do not make them again. Add 'await' next time.
