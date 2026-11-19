<!--
name: 'Slash Command: /mcp enable|disable — server already on/off'
description: >-
  Tells the model the named MCP server was already on or off, so nothing
  changed.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_1
  - SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_2
-->
MCP server "${SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_0(SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_1)}" is already ${SLASH_COMMAND_MCP_TOGGLE_SERVER_ALREADY_ON_OFF_VAR_2?"on":"off"}
