<!--
name: 'System Reminder: Projects reply gate silent turn'
description: >-
  Tells Claude its last turn sent no reply to the project thread and to call the
  reply, status or no-reply tool
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_0
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_1
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_2
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_3
-->
Your last turn ended without a reply to the project thread: plain text is not delivered there${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_0?", and a checklist is not a reply":""}. Call \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_1.toolNames.reply}\` now with what the thread should see, ${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_2?`\`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_1.toolNames.status}\` if you dispatched work that reports back later, `:""}or \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_3}\` if no reply is warranted.
