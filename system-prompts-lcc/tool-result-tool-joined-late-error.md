<!--
name: 'Tool result: ToolJoinedLateError'
description: >-
  Tool-use error telling the model a tool was not available when its call
  arrived and asking it to write the call again in full.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_TOOL_JOINED_LATE_ERROR_VAR_0
  - TOOL_RESULT_TOOL_JOINED_LATE_ERROR_VAR_1
-->
ToolJoinedLateError: ${TOOL_RESULT_TOOL_JOINED_LATE_ERROR_VAR_0} did not run. It was not available when this call arrived, so its input could not be checked as it would run. This is not a judgment that the call is unsafe.${TOOL_RESULT_TOOL_JOINED_LATE_ERROR_VAR_1?" The copy of its input kept in this conversation is cut short.":""} The tool is available now: write the call again in full.
