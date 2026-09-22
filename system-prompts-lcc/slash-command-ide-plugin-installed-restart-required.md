<!--
name: 'Slash Command: /ide — plugin installed, IDE restart required'
description: >-
  Tells the model the plugin landed at a specific path but will not take effect
  until the IDE is fully restarted, which is a precondition for anything that
  depends on the integration.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_0
  - SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_1
  - SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_2
-->
Installed plugin to ${SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_0.bold(SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_1(SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_2))}
Please ${SLASH_COMMAND_IDE_PLUGIN_INSTALLED_RESTART_REQUIRED_VAR_0.bold("restart your IDE")} completely for it to take effect
