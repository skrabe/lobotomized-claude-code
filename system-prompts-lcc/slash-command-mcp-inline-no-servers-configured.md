<!--
name: 'Slash Command: /mcp — No Servers Configured (Inline)'
description: >-
  Inline /mcp reply when no MCP servers are configured, with an add or open hint
  that fits the surface and the usage line.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_0
  - SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_1
  - SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_2
-->
No MCP servers are configured.${SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_0(" Add one with `claude mcp add`."," Open MCP servers from the command menu.")}${SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_1()?"":`
${SLASH_COMMAND_MCP_INLINE_NO_SERVERS_CONFIGURED_VAR_2}`}
