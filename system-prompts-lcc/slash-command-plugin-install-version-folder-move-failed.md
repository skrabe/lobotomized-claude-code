<!--
name: 'Slash Command: /plugin Install Failed To Move New Copy Into Version Folder'
description: >-
  Error returned when a plugin install cannot move the freshly staged copy into
  its version folder. It gives the cause, what happened to any previously
  installed copy and to leftover paths, and a retry hint.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_3
  - SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_4
-->
Could not move the new copy of this plugin version into ${SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_0}: ${SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_1}.${SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_2}${SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_3} ${SLASH_COMMAND_PLUGIN_INSTALL_VERSION_FOLDER_MOVE_FAILED_VAR_4?"Run the install again once other Claude Code sessions or programs using that folder have finished.":"Check the plugin cache folder's permissions and free disk space, then run the install again."}
