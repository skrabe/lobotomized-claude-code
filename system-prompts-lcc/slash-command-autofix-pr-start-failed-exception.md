<!--
name: 'Slash command: /autofix-pr couldn''t start (exception)'
description: >-
  The same lead for an exception thrown while starting /autofix-pr; the error
  message follows. Reaches the model as local-command-stdout.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_0
  - SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_1
  - SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_2
-->
Couldn't start autofix: ${SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_0 instanceof SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_1?SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_0.message:SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_2(SLASH_COMMAND_AUTOFIX_PR_START_FAILED_EXCEPTION_VAR_0)}
