<!--
name: 'Tool Result: MCP response over size cap'
description: >-
  Error returned when an MCP tool response exceeded the size cap and was not
  read, warning the tool may have run.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_0
  - TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_1
  - TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_2
  - TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_3
-->
The response from MCP server "${TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_0}" for tool "${TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_1}" was larger than ${TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_2.round(TOOL_RESULT_MCP_RESPONSE_TOO_LARGE_NOT_READ_VAR_3.capBytes/1024/1024)}MB, so it was not read. The tool may have run: check whether it did before running it again, and when you run it again, ask for less data.
