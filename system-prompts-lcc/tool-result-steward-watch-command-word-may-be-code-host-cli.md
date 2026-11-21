<!--
name: 'Tool Result: Steward watch command word may be a code host CLI'
description: >-
  Hook refusal reason when a shell line has a word that may be a code host's
  command-line tool, telling Claude to tell the user if it only names a file or
  test
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_WATCH_COMMAND_WORD_MAY_BE_CODE_HOST_CLI_VAR_0
-->
this line has the word \`${TOOL_RESULT_STEWARD_WATCH_COMMAND_WORD_MAY_BE_CODE_HOST_CLI_VAR_0}\`, which may be a code host's command-line tool, and this watch doesn't run those. If it only names a file or a test, tell the user so
