<!--
name: 'Slash Command: /plugin validate .mcp.json invalid JSON'
description: >-
  /plugin validate error for an MCP server file with invalid JSON syntax,
  including a note that this file must not have a UTF-8 BOM.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_2
-->
Invalid JSON syntax: ${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_0.content.startsWith("﻿")?"the file starts with a UTF-8 byte-order mark (BOM), which this file (unlike plugin.json) must not have — re-save it as UTF-8 without BOM":SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_1(SLASH_COMMAND_PLUGIN_VALIDATE_MCP_JSON_INVALID_SYNTAX_VAR_2)}. The plugin loader logs this at debug level and loads no servers from the file.
