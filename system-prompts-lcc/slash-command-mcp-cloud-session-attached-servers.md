<!--
name: 'Slash command: MCP cloud session attached servers'
description: >-
  /mcp note in a cloud session that attached machines' servers are managed
  there.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_0
  - SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_1
-->


Servers on ${SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_0.map(SLASH_COMMAND_MCP_CLOUD_SESSION_ATTACHED_SERVERS_VAR_1).join(", ")} are managed there — run \`/mcp\` in a terminal on that machine. A server that didn't start or is disabled there won't appear here, and its connection type isn't reported to the cloud session.
