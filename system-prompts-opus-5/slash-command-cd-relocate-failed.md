<!--
name: 'Slash Command: /cd — relocation failed, staying put'
description: >-
  Tells the model the move was attempted and failed, names the two likely
  causes, and states which directory the session is actually in — the fact it
  needs to keep using correct paths.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_0
  - SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_1
  - SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_2
-->
Couldn't move to ${SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_0.bold(SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_1)} — the directory may no longer exist, or the session couldn't be moved. Staying in ${SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_0.bold(SLASH_COMMAND_CD_RELOCATE_FAILED_VAR_2())}.
