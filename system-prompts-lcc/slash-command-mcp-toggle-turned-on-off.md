<!--
name: 'Slash Command: /mcp enable|disable — server turned on/off'
description: Confirms the single named MCP server was turned on or off.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_1
  - SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_2
-->
Turned ${SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_0?"on":"off"} MCP server "${SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_1(SLASH_COMMAND_MCP_TOGGLE_TURNED_ON_OFF_VAR_2)}"
