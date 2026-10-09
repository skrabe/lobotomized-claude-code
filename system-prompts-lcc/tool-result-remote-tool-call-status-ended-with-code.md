<!--
name: 'Tool Result: Remote tool call status — ended with code'
description: >-
  Default status clause naming the code a failed remote tool call ended with and
  when.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_REMOTE_TOOL_CALL_STATUS_ENDED_WITH_CODE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_CALL_STATUS_ENDED_WITH_CODE_VAR_1
-->
it ended as ${TOOL_RESULT_REMOTE_TOOL_CALL_STATUS_ENDED_WITH_CODE_VAR_0.code??"failed"} at ${TOOL_RESULT_REMOTE_TOOL_CALL_STATUS_ENDED_WITH_CODE_VAR_1} UTC
