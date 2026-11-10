<!--
name: File shown with escaped closing reminder tags
description: >-
  Meta note that a file's closing system-reminder tags are shown with &lt;
  instead of < so they cannot end the reminder.
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_FILE_CLOSING_REMINDER_TAGS_ESCAPED_NOTE_VAR_0
  - SYSTEM_REMINDER_FILE_CLOSING_REMINDER_TAGS_ESCAPED_NOTE_VAR_1
-->
Note: ${SYSTEM_REMINDER_FILE_CLOSING_REMINDER_TAGS_ESCAPED_NOTE_VAR_0(SYSTEM_REMINDER_FILE_CLOSING_REMINDER_TAGS_ESCAPED_NOTE_VAR_1)} is not shown exactly as it is on disk. Each closing system-reminder tag in it starts with \`<\` on disk and is shown above with \`&lt;\` instead, so that it cannot end the reminder around the text.
