<!--
name: MCP Server Disabled In Another Session
description: >-
  Returned by /mcp reconnect/enable when the named server was disabled in
  another session, so this session must disable and re-enable (or restart) to
  reconnect.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_0
  - SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_1
-->
"${SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_0(SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_1)}" was disabled in another session — disable and re-enable it in /mcp, or restart, to reconnect
