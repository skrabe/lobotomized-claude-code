<!--
name: 'Tool result: write permission ask for Claude settings file'
description: >-
  Permission ask message when Claude requests to write a Claude Code settings
  file, with optional link note
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_0
  - TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_1
  - TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_2
-->
Claude requested permissions to write to ${TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_0(TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_1)}, but you haven't granted it yet.${TOOL_RESULT_WRITE_SETTINGS_FILE_ASK_VAR_2}
