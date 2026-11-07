<!--
name: 'Tool Result: MCP connector raw call refused (tool name unchecked)'
description: >-
  Refuses a raw connector call whose tool name cannot be checked without a tool
  list and suggests reconnecting via /mcp
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TOOL_NAME_NOT_CHECKED_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TOOL_NAME_NOT_CHECKED_VAR_0} was not called: Claude Code asked the model for a file's path for a tool of this connector but has no list of this connector's tools that shows any tool, and this call's tool name is not one it can check without one. Calling again may or may not work: reconnecting the connector lists its tools again (in a terminal: /mcp).
