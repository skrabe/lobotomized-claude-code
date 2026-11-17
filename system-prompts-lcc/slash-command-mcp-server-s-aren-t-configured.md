<!--
name: 'Slash Command: /mcp servers aren''t configured'
description: >-
  Says servers disabled in another session are not configured yet, so there is
  nothing to reconnect
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_0
  - SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_1
-->
${SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_0} MCP ${SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_1(SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_0,"server was","servers were")} disabled in another session but ${SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_1(SLASH_COMMAND_MCP_SERVER_S_AREN_T_CONFIGURED_VAR_0,"isn't","aren't")} configured yet, so there's nothing to reconnect.
