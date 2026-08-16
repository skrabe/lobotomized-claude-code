<!--
name: 'Slash Command: /mcp — new credentials rejected on reconnect'
description: >-
  Tells the model the fresh OAuth tokens were refused by the server and gives
  two recovery paths (re-authenticate, or restart), so it does not loop on the
  same flow.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_OAUTH_CREDENTIALS_REJECTED_VAR_0
-->
Got new credentials, but ${SLASH_COMMAND_MCP_OAUTH_CREDENTIALS_REJECTED_VAR_0.name} rejected them on reconnect. Try re-authenticating, or restart Claude Code if it persists.
