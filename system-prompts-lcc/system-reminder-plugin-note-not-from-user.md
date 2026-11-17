<!--
name: 'System Reminder: Plugin note, not from the user'
description: >-
  Wraps a note a plugin added to the conversation, labeling it as from the
  plugin and not from the user
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_0
  - SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_1
  - SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_2
-->
Note from ${SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_0}, not from the user:
${SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_1.map(SYSTEM_REMINDER_PLUGIN_NOTE_NOT_FROM_USER_VAR_2).join(`
`)}
