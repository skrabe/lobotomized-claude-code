<!--
name: '/resume: multiple sessions match'
description: >-
  /resume result when several sessions match the argument, telling the user to
  run /resume to pick one.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_RESUME_MULTIPLE_MATCHES_VAR_0
  - SLASH_COMMAND_RESUME_MULTIPLE_MATCHES_VAR_1
-->
Found ${SLASH_COMMAND_RESUME_MULTIPLE_MATCHES_VAR_0.count} sessions matching ${SLASH_COMMAND_RESUME_MULTIPLE_MATCHES_VAR_1.bold(SLASH_COMMAND_RESUME_MULTIPLE_MATCHES_VAR_0.arg)}. Run /resume to pick one.
