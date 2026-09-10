<!--
name: 'Tool Result: GetTask Cancelled Output So Far'
description: >-
  GetTask statusMessage when a background shell was killed, including
  output-so-far path.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_0
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_1
  - TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_2
-->
The command was ${TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_0?TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_1[v]:"stopped before it completed"}. Output so far: ${TOOL_RESULT_GETTASK_CANCELLED_OUTPUT_SO_FAR_VAR_2}
