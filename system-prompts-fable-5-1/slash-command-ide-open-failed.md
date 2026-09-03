<!--
name: 'Slash Command: /ide — launch failed, open manually'
description: >-
  Tells the model the editor launch exited non-zero and gives the path to open
  by hand as the fallback.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_IDE_OPEN_FAILED_VAR_0
  - SLASH_COMMAND_IDE_OPEN_FAILED_VAR_1
-->
Failed to open in ${SLASH_COMMAND_IDE_OPEN_FAILED_VAR_0.name}. Try opening manually: ${SLASH_COMMAND_IDE_OPEN_FAILED_VAR_1}
