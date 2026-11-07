<!--
name: 'Slash Command: /rename partial failure summary'
description: >-
  Joins the rename result with its update warnings and points to --debug for the
  cause
ccVersion: 2.1.319
variables:
  - SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_0
  - SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_1
  - SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_2
-->
${SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_0}. ${SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_1.join(". ")}${SLASH_COMMAND_RENAME_PARTIAL_FAILURE_DEBUG_HINT_VAR_2} (run with --debug for the cause)
