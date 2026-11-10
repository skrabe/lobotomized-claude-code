<!--
name: MCP tool result arrived without text
description: >-
  Error that an MCP tool result arrived without its text, likely too large,
  telling Claude to check whether it ran and ask for less
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_TOOL_RESULT_ARRIVED_WITHOUT_TEXT_VAR_0
  - TOOL_RESULT_MCP_TOOL_RESULT_ARRIVED_WITHOUT_TEXT_VAR_1
-->
The result of MCP tool "${TOOL_RESULT_MCP_TOOL_RESULT_ARRIVED_WITHOUT_TEXT_VAR_0}" on server "${TOOL_RESULT_MCP_TOOL_RESULT_ARRIVED_WITHOUT_TEXT_VAR_1}" arrived without its text. A result that is too large arrives this way. The tool may have run: check whether it did before running it again, and when you run it again, ask for less data.
