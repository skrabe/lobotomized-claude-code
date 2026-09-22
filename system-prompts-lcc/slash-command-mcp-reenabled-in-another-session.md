<!--
name: MCP Server Re-Enabled In Another Session
description: >-
  Returned by /mcp disable when a concurrent session re-enabled the server,
  explaining that the disable did not persist and how to make it stick.
ccVersion: 2.1.221
variables:
  - SLASH_COMMAND_MCP_REENABLED_IN_ANOTHER_SESSION_VAR_0
-->

"${SLASH_COMMAND_MCP_REENABLED_IN_ANOTHER_SESSION_VAR_0}" was re-enabled in another session, so this disable didn't persist — /mcp enable ${SLASH_COMMAND_MCP_REENABLED_IN_ANOTHER_SESSION_VAR_0} then /mcp disable ${SLASH_COMMAND_MCP_REENABLED_IN_ANOTHER_SESSION_VAR_0} makes it stick. Left alone, it connects on the next launch.
