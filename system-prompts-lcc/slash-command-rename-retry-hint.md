<!--
name: 'Slash Command: /rename retry hint'
description: >-
  Suffix telling the user to run /rename again with the requested or new name
  when the transcript could not be updated
ccVersion: 2.1.319
variables:
  - SLASH_COMMAND_RENAME_RETRY_HINT_VAR_0
  - SLASH_COMMAND_RENAME_RETRY_HINT_VAR_1
  - SLASH_COMMAND_RENAME_RETRY_HINT_VAR_2
-->
. Run /rename ${SLASH_COMMAND_RENAME_RETRY_HINT_VAR_0.registryUpdated?SLASH_COMMAND_RENAME_RETRY_HINT_VAR_1:SLASH_COMMAND_RENAME_RETRY_HINT_VAR_2} to try again
