<!--
name: 'Tool Result: REPL refused calls more count'
description: Trailing row in the REPL refused-calls note counting refused calls not listed.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REPL_REFUSED_CALLS_MORE_COUNT_VAR_0
  - TOOL_RESULT_REPL_REFUSED_CALLS_MORE_COUNT_VAR_1
-->
- and ${TOOL_RESULT_REPL_REFUSED_CALLS_MORE_COUNT_VAR_0} more refused ${TOOL_RESULT_REPL_REFUSED_CALLS_MORE_COUNT_VAR_1(TOOL_RESULT_REPL_REFUSED_CALLS_MORE_COUNT_VAR_0,"call")}
