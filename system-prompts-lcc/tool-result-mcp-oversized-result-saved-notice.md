<!--
name: 'Tool Result: MCP oversized result saved notice'
description: >-
  Tells Claude that a tool result exceeded the token limit and was saved to a
  file, naming the path and format
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_0
  - TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_1
  - TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_2
-->
Error: result (${TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_0}) exceeds maximum allowed tokens. Output has been saved to ${TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_1}.
Format: ${TOOL_RESULT_MCP_OVERSIZED_RESULT_SAVED_NOTICE_VAR_2}
