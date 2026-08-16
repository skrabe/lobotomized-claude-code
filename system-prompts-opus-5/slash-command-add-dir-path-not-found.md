<!--
name: 'Slash Command: /add-dir — path not found'
description: >-
  Reports to the model that the requested directory does not exist on disk, so
  any plan that assumed that path is now accessible is invalid.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADD_DIR_PATH_NOT_FOUND_VAR_0
  - SLASH_COMMAND_ADD_DIR_PATH_NOT_FOUND_VAR_1
-->
Path ${SLASH_COMMAND_ADD_DIR_PATH_NOT_FOUND_VAR_0.bold(SLASH_COMMAND_ADD_DIR_PATH_NOT_FOUND_VAR_1.absolutePath)} was not found.
