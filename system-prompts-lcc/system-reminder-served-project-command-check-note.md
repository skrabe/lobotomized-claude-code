<!--
name: Served Project Command Check Note
description: >-
  Note added to a served call's PreToolUse hook result when the project's
  sandboxed command check asked, added context, or failed with stderr; joined
  into the hook's additionalContext for the cloud session's model.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_SERVED_PROJECT_COMMAND_CHECK_NOTE_VAR_0
  - SYSTEM_REMINDER_SERVED_PROJECT_COMMAND_CHECK_NOTE_VAR_1
-->
This project's command check (${SYSTEM_REMINDER_SERVED_PROJECT_COMMAND_CHECK_NOTE_VAR_0}) ${{asked:"asked for confirmation and said",context:"added this context",stderr:"did not finish; its first line of error output was"}[n]}: ${SYSTEM_REMINDER_SERVED_PROJECT_COMMAND_CHECK_NOTE_VAR_1}
