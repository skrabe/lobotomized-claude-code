<!--
name: 'Tool Result: Served project commands count'
description: Summarizes listed project commands and truncation or refusal counts.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_0
  - TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_1
  - TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_2
-->
${TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_0.length} commands${TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_1?", cut at a limit":""}${TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_2>0?`, ${TOOL_RESULT_SERVED_PROJECT_COMMANDS_COUNT_VAR_2} refused`:""}
