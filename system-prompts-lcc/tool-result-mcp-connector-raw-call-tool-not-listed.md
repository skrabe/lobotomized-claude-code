<!--
name: 'Tool Result: MCP connector raw call refused (tool not listed)'
description: >-
  Refuses a raw connector call whose tool name is not in the connector's tool
  list and suggests checking the name or reconnecting via /mcp
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TOOL_NOT_LISTED_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TOOL_NOT_LISTED_VAR_0} was not called: Claude Code asked the model for a file's path for a tool of this connector, and its list of this connector's tools has no tool under the exact name this call gave (it is shown here as Claude Code would show it), so it could not tell what this call would send. Check the name the call gave; if it is right, reconnecting the connector lists its tools again (in a terminal: /mcp), and the list may then hold such a tool.
