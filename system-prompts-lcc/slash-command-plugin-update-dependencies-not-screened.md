<!--
name: 'Plugin update: dependencies installed but not screened'
description: >-
  Failed update result: the plugin's listed packages installed but the check for
  links leading outside the plugin could not finish; includes the cause.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_2
  - SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_3
-->
Installed the packages that "${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_0}" lists for scope ${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_1}, but could not finish checking them for links that lead outside the plugin. Cause: ${SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_2(SLASH_COMMAND_PLUGIN_UPDATE_DEPENDENCIES_NOT_SCREENED_VAR_3)}
