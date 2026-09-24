<!--
name: 'Plugin Validate: MCP Undeclared User Config Reference'
description: >-
  Plugin-validate error that an MCP server field references a ${user_config.KEY}
  not declared under userConfig (or the server's channels entry), so it cannot
  resolve on a fresh install.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_UNDECLARED_USER_CONFIG_REFERENCE_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_MCP_UNDECLARED_USER_CONFIG_REFERENCE_VAR_1
-->
references \${user_config.${SLASH_COMMAND_PLUGIN_VALIDATE_MCP_UNDECLARED_USER_CONFIG_REFERENCE_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_MCP_UNDECLARED_USER_CONFIG_REFERENCE_VAR_1,64)}}, which plugin.json does not declare under "userConfig" (or in this server's "channels" entry), so on a fresh install it cannot resolve: the loader drops the server or passes the literal text through. Declare the option or fix the key.
