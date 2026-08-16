<!--
name: 'Slash Command: /resume — multiple sessions matched'
description: >-
  Tells the model the title was ambiguous and that the interactive picker is the
  way forward, so it does not retry the same argument.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_RESUME_MULTIPLE_SESSION_MATCHES_VAR_0
  - SLASH_COMMAND_RESUME_MULTIPLE_SESSION_MATCHES_VAR_1
-->
Found ${SLASH_COMMAND_RESUME_MULTIPLE_SESSION_MATCHES_VAR_0.count} sessions matching ${SLASH_COMMAND_RESUME_MULTIPLE_SESSION_MATCHES_VAR_1.bold(SLASH_COMMAND_RESUME_MULTIPLE_SESSION_MATCHES_VAR_0.arg)}. Please use /resume to pick a specific session.
