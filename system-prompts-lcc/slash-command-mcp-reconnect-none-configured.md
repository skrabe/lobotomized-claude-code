<!--
name: 'Slash command: MCP reconnect none configured'
description: >-
  /mcp reconnect all reply when the remaining servers aren't configured yet and
  the rest are connected.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_MCP_RECONNECT_NONE_CONFIGURED_VAR_0
  - SLASH_COMMAND_MCP_RECONNECT_NONE_CONFIGURED_VAR_1
-->
${SLASH_COMMAND_MCP_RECONNECT_NONE_CONFIGURED_VAR_0} MCP ${SLASH_COMMAND_MCP_RECONNECT_NONE_CONFIGURED_VAR_1(SLASH_COMMAND_MCP_RECONNECT_NONE_CONFIGURED_VAR_0,"server isn't","servers aren't")} configured yet, so there's nothing to reconnect. The rest are already connected or connecting.
