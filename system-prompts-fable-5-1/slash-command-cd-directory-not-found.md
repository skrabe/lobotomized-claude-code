<!--
name: 'Slash Command: /cd — no directory at that path'
description: >-
  Tells the model the requested path does not exist, so the working directory is
  unchanged and the path itself is the thing to correct.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_DIRECTORY_NOT_FOUND_VAR_0
  - SLASH_COMMAND_CD_DIRECTORY_NOT_FOUND_VAR_1
-->
Couldn't find a directory at ${SLASH_COMMAND_CD_DIRECTORY_NOT_FOUND_VAR_0.bold(SLASH_COMMAND_CD_DIRECTORY_NOT_FOUND_VAR_1.path)}.
