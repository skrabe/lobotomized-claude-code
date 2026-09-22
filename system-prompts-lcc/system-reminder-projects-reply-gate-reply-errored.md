<!--
name: 'System Reminder: Projects reply gate after tool error'
description: >-
  Tells the model its project-thread reply tool call errored so nothing was
  delivered, and to call the reply tool again or the no-reply tool.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_0
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_1
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_2
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_3
-->
${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_0} Your \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_1}\` call this turn returned an error, so nothing reached the project thread. Call \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_2}\` again with what the thread should see, or \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_REPLY_ERRORED_VAR_3}\` if no reply is warranted.
