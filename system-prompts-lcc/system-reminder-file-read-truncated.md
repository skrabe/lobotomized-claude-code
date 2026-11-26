<!--
name: File read truncated reminder
description: >-
  System-reminder appended to a file Read result telling the model the view is
  paginated and to page with offset/limit.
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_0
  - SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_1
  - SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_2
-->
${SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_0(SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_1.filePath)}: showing ${SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_1.numLines} of ${SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_1.totalLines} lines. Call ${SYSTEM_REMINDER_FILE_READ_TRUNCATED_VAR_2} with offset/limit to page through.]
