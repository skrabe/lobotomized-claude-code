<!--
name: 'Slash Command: MCP server disabled in another session'
description: >-
  Returned by the /mcp slash command when enabling a server that another session
  disabled; explains the server still works this session but will not reconnect
  on next launch.
ccVersion: 2.1.221
variables:
  - SLASH_COMMAND_MCP_SERVER_DISABLED_IN_ANOTHER_SESSION_VAR_0
-->

"${SLASH_COMMAND_MCP_SERVER_DISABLED_IN_ANOTHER_SESSION_VAR_0}" is still available in this session, but another session disabled it — it keeps working here and won't reconnect after the next launch. Disable and re-enable it in /mcp to persist the re-enable.
