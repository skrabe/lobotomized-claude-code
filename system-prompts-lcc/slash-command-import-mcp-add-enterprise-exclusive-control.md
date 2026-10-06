<!--
name: '/import: MCP add blocked by enterprise MCP config'
description: >-
  Error line /import reports when enterprise MCP configuration has exclusive
  control over MCP servers.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_IMPORT_MCP_ADD_ENTERPRISE_EXCLUSIVE_CONTROL_VAR_0
-->
Cannot add MCP server: enterprise MCP configuration is active and has exclusive control over MCP servers${SLASH_COMMAND_IMPORT_MCP_ADD_ENTERPRISE_EXCLUSIVE_CONTROL_VAR_0===null?"":`. ${SLASH_COMMAND_IMPORT_MCP_ADD_ENTERPRISE_EXCLUSIVE_CONTROL_VAR_0}`}
