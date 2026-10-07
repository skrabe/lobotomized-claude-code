<!--
name: 'System Reminder: @-mention reference too large'
description: >-
  Meta message for an @-mentioned file too large to attach, telling the model to
  read it in portions with offset/limit or search instead
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_1
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_2
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_3
-->
${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_0} (${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_1(SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_2.fileSize)}). Its contents were not attached because the file is too large to read all at once, and a ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_3} call with no limit parameter will fail. Read it in portions with the offset and limit parameters, starting with a few hundred lines, or search for specific content instead of reading the whole file.
