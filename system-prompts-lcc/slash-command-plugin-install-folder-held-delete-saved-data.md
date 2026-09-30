<!--
name: 'Slash Command: Plugin Install Folder Held Delete Saved Data'
description: >-
  Instruction to let /plugin delete the plugin's saved data, otherwise the new
  plugin would start with it.
ccVersion: 2.1.285
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_FOLDER_HELD_DELETE_SAVED_DATA_VAR_0
-->
${SLASH_COMMAND_PLUGIN_INSTALL_FOLDER_HELD_DELETE_SAVED_DATA_VAR_0==="ui"?"When it asks":"If /plugin asks"}, let it delete the plugin's saved data: the new plugin would otherwise start with it.
