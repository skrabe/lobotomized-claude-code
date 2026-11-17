<!--
name: 'Slash Command: /branch — switched to the new branch'
description: >-
  /branch output after switching into the branched session, with how to get back
  to the original.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_0
  - SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_1
  - SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_2
  - SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_3
-->
Branched session${SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_0}. You're now in the new one (${SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_1}). Back to the original: /resume ${SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_2}${SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_3}, or \`claude -r ${SLASH_COMMAND_BRANCH_SWITCHED_TO_NEW_SESSION_VAR_2}\` in a new terminal.
