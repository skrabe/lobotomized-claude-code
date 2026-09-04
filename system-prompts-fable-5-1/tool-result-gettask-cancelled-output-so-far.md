<!--
name: 'GetTask: Command Stopped With Output So Far'
description: >-
  GetTask snapshot statusMessage when a local-shell command is killed, returned
  to the model as the cancelled task result.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_0
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_1
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_2
-->
The command was ${TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_0?TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_1[E]:"stopped before it completed"}. Output so far: ${TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_2}
