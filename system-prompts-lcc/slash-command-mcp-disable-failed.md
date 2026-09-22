<!--
name: 'Slash Command: /mcp — Disable Failed'
description: >-
  Inline /mcp reply when disabling a named server failed because it may have
  been removed or its config could not be read. It ends with a hint, fitted to
  the surface, to check /mcp.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_0
  - SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_1
  - SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_2
-->
Couldn't disable "${SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_0(SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_1)}" — it may have been removed, or its configuration couldn't be read.${SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_2(" Run `/mcp` in the terminal to check."," Open MCP servers from the command menu.")}
