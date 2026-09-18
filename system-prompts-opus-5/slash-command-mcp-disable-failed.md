<!--
name: MCP disable failed
description: >-
  /mcp disable failure when the server may have been removed or its config could
  not be read; returned as local-command-stdout.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_0
  - SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_1
-->
Couldn't disable "${SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_0(SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_1)}" — it may have been removed, or its configuration couldn't be read.${SLASH_COMMAND_MCP_DISABLE_FAILED_VAR_2(" Run `/mcp` in the terminal to check."," Open MCP servers from the command menu.")}
