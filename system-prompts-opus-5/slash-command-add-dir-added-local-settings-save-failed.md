<!--
name: 'Slash Command: /add-dir — added but persisting failed'
description: >-
  Tells the model the directory works for now but the settings write failed,
  with the error text, so it knows the grant will not survive a restart.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_0
  - SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_1
  - SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_2
  - SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_3
-->
Added ${SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_0.bold(SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_1)} as a working directory. Failed to save to local settings: ${SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_2 instanceof SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_3?SLASH_COMMAND_ADD_DIR_ADDED_LOCAL_SETTINGS_SAVE_FAILED_VAR_2.message:"Unknown error"}
