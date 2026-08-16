<!--
name: 'Slash Command: /mcp — bulk disable didn''t persist, re-enabled elsewhere'
description: >-
  Tells the model that a `/mcp disable all` silently failed to persist for N
  servers and gives the enable-then-disable recovery, so it does not report the
  disable as done.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_BULK_REENABLED_IN_ANOTHER_SESSION_VAR_0
-->
${SLASH_COMMAND_MCP_BULK_REENABLED_IN_ANOTHER_SESSION_VAR_0} MCP server(s) were re-enabled in another session, so this disable didn't persist for them — enable then disable each in /mcp to make it stick. Left alone, they connect on the next launch.
