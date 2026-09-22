<!--
name: 'Cloud session: project command check stopped after repeated asks'
description: >-
  Hook additionalContext for a cloud-served call when the project's command
  check needed the person's OK three times in a row: it is not run again this
  session, each command asks instead, and how the person can stop the questions.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_CLOUD_SESSION_COMMAND_CHECK_STOPPED_AFTER_REPEATED_ASKS_VAR_0
-->
This project's command check (${TOOL_RESULT_CLOUD_SESSION_COMMAND_CHECK_STOPPED_AFTER_REPEATED_ASKS_VAR_0}) needed the person's OK three times in a row on this computer, so it is not run again for this session and each command asks instead. To stop the questions, the person can review the check and define it in ~/.claude/settings.json on that computer; if it could not finish there, make it work read-only (no writes outside $TMPDIR, no network, no tools installed under the home directory).
