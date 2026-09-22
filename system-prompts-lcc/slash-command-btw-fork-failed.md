<!--
name: 'Slash Command: /btw — fork failed'
description: >-
  Reports that the requested side-question fork never started and carries the
  underlying error, so the model explains the failure instead of assuming a
  subagent is running.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_BTW_FORK_FAILED_VAR_0
  - SLASH_COMMAND_BTW_FORK_FAILED_VAR_1
-->
Failed to fork: ${SLASH_COMMAND_BTW_FORK_FAILED_VAR_0(SLASH_COMMAND_BTW_FORK_FAILED_VAR_1)}
