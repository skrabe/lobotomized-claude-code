<!--
name: MCP Server Disabled In Another Session
description: >-
  Returned by /mcp enable when the named server was disabled by a concurrent
  session, telling the reader the enable did not take effect until it is
  re-toggled in the terminal /mcp UI.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_0
-->
"${SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_0(SLASH_COMMAND_MCP_DISABLED_IN_ANOTHER_SESSION_VAR_1)}" was disabled in another session — disable and re-enable it in /mcp, or restart, to reconnect
