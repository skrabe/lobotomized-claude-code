<!--
name: 'Plugin update: command source disabled'
description: >-
  Explains that a command-installed plugin's install command was not run because
  the plugin is disabled, and tells the user to enable it first.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_2
  - SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_3
-->
${SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_0(SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_1,200)} is disabled, so the command that installs it was not run. Enable it first, then ${SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_2("plugin update",SLASH_COMMAND_PLUGIN_UPDATE_COMMAND_SOURCE_DISABLED_VAR_3,{extra:ve,fallback:"update it explicitly"})}.
