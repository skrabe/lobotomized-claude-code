<!--
name: 'Tool result: async REPL calls still running at script end'
description: >-
  Async-REPL warning that tool calls still run after the script ended;
  .then(self.log) output arrives as late output; do not re-issue.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_ASYNC_CALLS_STILL_RUNNING_AT_SCRIPT_END_VAR_0
  - TOOL_RESULT_REPL_ASYNC_CALLS_STILL_RUNNING_AT_SCRIPT_END_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_ASYNC_CALLS_STILL_RUNNING_AT_SCRIPT_END_VAR_0.length} tool call(s) still running at script end (${TOOL_RESULT_REPL_ASYNC_CALLS_STILL_RUNNING_AT_SCRIPT_END_VAR_1}) — they run on and their effects happen; what a .then(self.log) logs arrives as late output, anything else is not in this result. Do not re-issue them; await next time.
