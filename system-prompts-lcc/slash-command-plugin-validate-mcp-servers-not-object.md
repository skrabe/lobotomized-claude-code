<!--
name: 'Slash Command: /plugin validate MCP servers not an object'
description: >-
  /plugin validate error when an MCP server file's servers value is neither an
  object nor an array, so no servers load from the file.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_SERVERS_NOT_OBJECT_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_SERVERS_NOT_OBJECT_VAR_1
-->
must be an object mapping server names to server configs (got ${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_SERVERS_NOT_OBJECT_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_MCP_SERVERS_NOT_OBJECT_VAR_1)}). No servers load from this file.
