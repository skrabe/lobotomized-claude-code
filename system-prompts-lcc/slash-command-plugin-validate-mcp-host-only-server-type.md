<!--
name: '/plugin validate: host-only server type'
description: >-
  Error that a host-only MCP server type cannot be declared by a plugin and is
  dropped at load.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_HOST_ONLY_SERVER_TYPE_VAR_0
-->
type "${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_HOST_ONLY_SERVER_TYPE_VAR_0.data.type}" servers are registered by the host application at runtime and cannot be declared by a plugin. The plugin loader drops this server at load.
