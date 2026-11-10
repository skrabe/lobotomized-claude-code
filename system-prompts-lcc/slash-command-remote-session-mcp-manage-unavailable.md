<!--
name: 'Slash Command: Remote session MCP management unavailable'
description: >-
  Result when /mcp is run in a remote session, pointing to the claude.ai
  Connectors page.
ccVersion: 2.1.322
variables:
  - SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_0
  - SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_1
  - SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_2
-->
Managing connectors (MCP servers) by command isn't available here. To manage them, open the Connectors page on claude.ai: ${SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_0(SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_1,SLASH_COMMAND_REMOTE_SESSION_MCP_MANAGE_UNAVAILABLE_VAR_2.SESSION_INGRESS_URL)}/customize/connectors
