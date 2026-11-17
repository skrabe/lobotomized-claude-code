<!--
name: 'Slash command: MCP reconnect all disabled enable all'
description: >-
  /mcp reconnect all note that servers are disabled and /mcp enable all brings
  them back.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_0
  - SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_1
-->
${SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_0} MCP ${SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_1(SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_0,"server is","servers are")} disabled. Run \`/mcp enable all\` to bring ${SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_1(SLASH_COMMAND_MCP_RECONNECT_ALL_DISABLED_ENABLE_ALL_VAR_0,"it","them")} back.
