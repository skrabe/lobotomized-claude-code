<!--
name: 'Slash Command: /plugin-types Wrote Declarations'
description: >-
  /plugin-types success text reporting how many MCP tools and servers were
  written into claude-code-mcp.d.ts.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_0
  - SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_1
  - SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_2
  - SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_3
-->
Wrote ${SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_0}: ${SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_1.length} MCP ${SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_2(SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_1.length,"tool")} from ${SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_3.size} ${SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_2(SLASH_COMMAND_PLUGIN_TYPES_WROTE_VAR_3.size,"server")}. Include it in the plugin's tsconfig beside the engine's "claude-code" module types, and e narrows per tool.
