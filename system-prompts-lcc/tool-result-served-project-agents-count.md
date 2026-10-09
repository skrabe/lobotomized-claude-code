<!--
name: 'Tool Result: Served project agents count'
description: Summarizes the number of listed project agents and truncation.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_PROJECT_AGENTS_COUNT_VAR_0
  - TOOL_RESULT_SERVED_PROJECT_AGENTS_COUNT_VAR_1
-->
${TOOL_RESULT_SERVED_PROJECT_AGENTS_COUNT_VAR_0.length} agents${TOOL_RESULT_SERVED_PROJECT_AGENTS_COUNT_VAR_1?", cut at a limit":""}
