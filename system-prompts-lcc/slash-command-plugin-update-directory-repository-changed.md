<!--
name: 'Plugin Update: Directory Lists Different Repository'
description: >-
  Update failure when the plugin directory now lists a different repository
  under the plugin's name; tells the user to uninstall it and then install the
  new listing if they want it.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_0(SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_1)}" was not updated: the ${SLASH_COMMAND_PLUGIN_UPDATE_DIRECTORY_REPOSITORY_CHANGED_VAR_2} now lists a different repository under that name. Uninstall it, then install the new listing if you want it.
