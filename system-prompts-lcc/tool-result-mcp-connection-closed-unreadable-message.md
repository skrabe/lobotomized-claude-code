<!--
name: 'Tool Result: MCP connection closed on unreadable message'
description: >-
  Error returned when the MCP connection closed because a server message was too
  large or unparseable, so the tool result was not read.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_MCP_CONNECTION_CLOSED_UNREADABLE_MESSAGE_VAR_0
  - TOOL_RESULT_MCP_CONNECTION_CLOSED_UNREADABLE_MESSAGE_VAR_1
-->
The connection to MCP server "${TOOL_RESULT_MCP_CONNECTION_CLOSED_UNREADABLE_MESSAGE_VAR_0}" was closed because a message from the server was too large or could not be parsed, so the result of tool "${TOOL_RESULT_MCP_CONNECTION_CLOSED_UNREADABLE_MESSAGE_VAR_1}" was not read. The tool may have run: check whether it did before running it again.
