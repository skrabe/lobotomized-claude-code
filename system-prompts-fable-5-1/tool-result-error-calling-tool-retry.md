<!--
name: 'Tool Result: Error Calling Tool (retry)'
description: >-
  Generic isError tool_result content returned when a tool call throws, telling
  the model to try again with the underlying message.
ccVersion: 2.1.178
variables:
  - TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_0
  - TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_1
  - TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_2
-->
Error calling tool, please try again. : ${TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_0 instanceof TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_1?TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_0.message:TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_2(TOOL_RESULT_ERROR_CALLING_TOOL_RETRY_VAR_0)}
