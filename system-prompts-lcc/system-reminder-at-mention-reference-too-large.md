<!--
name: 'System Reminder: @-mention reference too large'
description: >-
  Meta message for an @-mentioned file too large to attach, telling the model to
  read it in portions with offset/limit or search instead
ccVersion: 2.1.296
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_1
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_2
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_3
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_4
-->
${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_0} (${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_1(SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_2.fileSize)}). Its contents were not attached because the file is too large to read all at once. Read it in portions with the offset and limit parameters, starting with a few hundred lines, or search for specific content instead of reading the whole file. Only if you genuinely need all of it, call ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_3} with ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_TOO_LARGE_VAR_4}: true, which reads it whole when it still fits in your context.
