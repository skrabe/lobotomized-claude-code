<!--
name: 'Slash Command: /cd — already in that directory'
description: >-
  Tells the model the move was a no-op because the session is already there, so
  it does not treat the directory as newly changed.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_ALREADY_IN_DIRECTORY_VAR_0
  - SLASH_COMMAND_CD_ALREADY_IN_DIRECTORY_VAR_1
-->
Already in ${SLASH_COMMAND_CD_ALREADY_IN_DIRECTORY_VAR_0.bold(SLASH_COMMAND_CD_ALREADY_IN_DIRECTORY_VAR_1.directory)}.
