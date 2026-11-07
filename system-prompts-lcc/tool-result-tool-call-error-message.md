<!--
name: 'Tool Result: Tool call error message'
description: >-
  Wraps the error thrown during a tool call in tool_use_error tags with an
  optional suffix as the tool_result content
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_TOOL_CALL_ERROR_MESSAGE_VAR_0
  - TOOL_RESULT_TOOL_CALL_ERROR_MESSAGE_VAR_1
-->
<tool_use_error>${TOOL_RESULT_TOOL_CALL_ERROR_MESSAGE_VAR_0.message}</tool_use_error>${TOOL_RESULT_TOOL_CALL_ERROR_MESSAGE_VAR_1??""}
