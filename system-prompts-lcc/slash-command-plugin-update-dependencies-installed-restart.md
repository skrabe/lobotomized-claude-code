<!--
name: 'Plugin update: dependencies installed, restart to apply'
description: >-
  Update result message saying the plugin's listed packages were installed for
  the scope and a restart is needed, followed by the underlying update message.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_2
-->
Installed the packages that "${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_0}" lists for scope ${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_1}. Restart to apply changes. ${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_INSTALLED_RESTART_VAR_2.message}
