<!--
name: 'Slash Command: /add-dir — path is a file, suggests parent'
description: >-
  Tells the model the path resolved to a file rather than a directory and names
  the parent directory as the recovery target.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_0
  - SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_1
  - SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_2
-->
${SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_0.bold(SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_1.directoryPath)} is not a directory. Did you mean to add the parent directory ${SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_0.bold(SLASH_COMMAND_ADD_DIR_NOT_A_DIRECTORY_VAR_2)}?
