<!--
name: 'Slash Command: Project set but save failed'
description: >-
  /project output when the Project applies until restart but could not be saved
  to the local settings file
ccVersion: 2.1.318
variables:
  - SLASH_COMMAND_PROJECT_SET_SAVE_FAILED_VAR_0
  - SLASH_COMMAND_PROJECT_SET_SAVE_FAILED_VAR_1
-->
${SLASH_COMMAND_PROJECT_SET_SAVE_FAILED_VAR_0}, until Claude Code restarts. Couldn't save it in ${SLASH_COMMAND_PROJECT_SET_SAVE_FAILED_VAR_1}, so new sessions in this folder won't use it. Check that it holds valid JSON and that you can write to it, then try again.
