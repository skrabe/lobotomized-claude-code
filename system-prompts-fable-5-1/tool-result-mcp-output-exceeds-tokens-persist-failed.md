<!--
name: 'Tool Result: MCP Output Exceeds Tokens (persist failed)'
description: >-
  Tool_result error when an MCP result exceeds max tokens and saving to file
  failed; suggests pagination/filtering tools.
ccVersion: 2.1.178
variables:
  - TOOL_RESULT_MCP_OUTPUT_EXCEEDS_TOKENS_PERSIST_FAILED_VAR_0
  - TOOL_RESULT_MCP_OUTPUT_EXCEEDS_TOKENS_PERSIST_FAILED_VAR_1
-->
Error: result (${TOOL_RESULT_MCP_OUTPUT_EXCEEDS_TOKENS_PERSIST_FAILED_VAR_0.toLocaleString()} characters) exceeds maximum allowed tokens. Failed to save output to file: ${TOOL_RESULT_MCP_OUTPUT_EXCEEDS_TOKENS_PERSIST_FAILED_VAR_1.error}. If this MCP server provides pagination or filtering tools, use them to retrieve specific portions of the data.
