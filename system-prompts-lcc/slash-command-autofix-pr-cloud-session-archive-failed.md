<!--
name: /autofix-pr cloud session couldn't be stopped
description: >-
  Told the model that a started cloud session couldn't be stopped and may still
  work on the PR, with how to stop it.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_AUTOFIX_PR_CLOUD_SESSION_ARCHIVE_FAILED_VAR_0
  - SLASH_COMMAND_AUTOFIX_PR_CLOUD_SESSION_ARCHIVE_FAILED_VAR_1
-->
A cloud session had already started and Claude Code couldn't stop it, so it may still work on the PR. Stop it here: ${SLASH_COMMAND_AUTOFIX_PR_CLOUD_SESSION_ARCHIVE_FAILED_VAR_0(SLASH_COMMAND_AUTOFIX_PR_CLOUD_SESSION_ARCHIVE_FAILED_VAR_1.id,void 0,{from:"cli"})}
