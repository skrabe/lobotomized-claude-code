<!--
name: 'Slash Command: MCP Cloud Session Attached Servers'
description: >-
  Tells a cloud /mcp listing that attached-host servers are managed in a local
  terminal and that failed or disabled servers are omitted.
ccVersion: 2.1.261
variables:
  - SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_0
  - SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_1
-->


Servers on ${SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_0.map(SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_1).join(", ")} are managed there — run \`/mcp\` in a local terminal on that machine. A server that's failed or disabled there won't appear here, and its transport type isn't reported to the cloud session.
