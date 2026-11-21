<!--
name: 'Tool result: REPL late calls not made'
description: Late report line listing tool calls that came too late and were not made.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_0
  - TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_1
  - TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_2
  - TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_3
-->
Tool calls that came too late and were not made: ${TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_0(TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_1)}${TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_2.callsWhenOver>TOOL_RESULT_REPL_LATE_CALLS_NOT_MADE_VAR_3?" and more":""}.
