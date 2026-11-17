<!--
name: 'Slash Command: /cd — moved, MCP choices not saved'
description: >-
  Tells the model /cd moved the session to the named directory, but its MCP
  server approval choices could not be saved and will be asked again.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_0
  - SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_1
  - SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_2
-->
Moved to ${SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_0.bold(SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_1(SLASH_COMMAND_CD_MOVED_TO_MCP_CHOICES_NOT_SAVED_VAR_2))}. One or more MCP server choices couldn't be saved (check permissions on .claude/settings.local.json), so you'll be asked again next time.
