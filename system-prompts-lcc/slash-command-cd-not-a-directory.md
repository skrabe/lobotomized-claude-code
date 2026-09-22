<!--
name: 'Slash Command: /cd — path is a file, suggests its parent'
description: >-
  Tells the model the path resolved to a file rather than a directory and names
  the parent directory as the likely intended target.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_0
  - SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_1
-->
${SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_0.bold(SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_1.path)} is not a directory. Did you mean ${SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_0.bold(SLASH_COMMAND_CD_NOT_A_DIRECTORY_VAR_1.parent)}?
