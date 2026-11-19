<!--
name: 'System Reminder: Projects reply gate reply errored'
description: >-
  Tells Claude its project-thread reply call errored and to call the reply tool
  again or the no-reply tool
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_0
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_1
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_2
-->
Your \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_0}\` call this turn returned an error, so it did not reach the project thread. Call \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_1.toolNames.reply}\` again with what the thread should see, or \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_2}\` if no reply is warranted.
