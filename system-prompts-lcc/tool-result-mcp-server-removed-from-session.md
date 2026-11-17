<!--
name: 'Tool result: MCP server removed from session'
description: >-
  Error returned when a tool call targets an MCP server that was removed from
  this session, telling Claude to continue without it.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_SERVER_REMOVED_FROM_SESSION_VAR_0
-->
MCP server "${TOOL_RESULT_MCP_SERVER_REMOVED_FROM_SESSION_VAR_0.name}" was not called: it was removed from this session. Continue without it.
