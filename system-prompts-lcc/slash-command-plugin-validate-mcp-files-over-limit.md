<!--
name: 'Slash command: /plugin validate MCP files over limit'
description: >-
  Validation note that plugin.json names more MCP server files than the
  validator examines, so the rest must be validated separately.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_2
-->
plugin.json names more than ${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_0} MCP server files; ${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_1} ${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_2(SLASH_COMMAND_PLUGIN_VALIDATE_MCP_FILES_OVER_LIMIT_VAR_1,"file")} past that limit were not examined. The plugin loader reads them all, so validate those files separately.
