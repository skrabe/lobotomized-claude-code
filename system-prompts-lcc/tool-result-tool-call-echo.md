<!--
name: Tool call echo wrapper
description: >-
  Meta message echoing a tool invocation and its input back into the model's
  context.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_TOOL_CALL_ECHO_VAR_0
  - TOOL_RESULT_TOOL_CALL_ECHO_VAR_1
  - TOOL_RESULT_TOOL_CALL_ECHO_VAR_2
-->
Called the ${TOOL_RESULT_TOOL_CALL_ECHO_VAR_0} tool with the following input: ${TOOL_RESULT_TOOL_CALL_ECHO_VAR_1(TOOL_RESULT_TOOL_CALL_ECHO_VAR_2)}
