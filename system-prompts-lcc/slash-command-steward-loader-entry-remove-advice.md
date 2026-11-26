<!--
name: 'Slash command: steward loader entry remove advice'
description: >-
  Else-arm of Na: start claude without the loader entry and remove it from
  settings or plugins; set it only in test scripts
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_STEWARD_LOADER_ENTRY_REMOVE_ADVICE_VAR_0
-->
Start claude from a shell without that entry, and take it out of Claude Code's settings or a plugin if one sets ${SLASH_COMMAND_STEWARD_LOADER_ENTRY_REMOVE_ADVICE_VAR_0}. If your tests need it, set it in the script that runs them
