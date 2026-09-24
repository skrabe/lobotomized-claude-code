<!--
name: 'System Reminder: Dir Sync Name List Overflow Suffix'
description: >-
  List formatter bn() used throughout the directory-sync notices: joins up to 12
  names and appends ' and [at least] N more' or ' and more' when the list is cut
  short.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_2
-->
${SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_0.join(", ")}${SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_1>0?` and ${SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_2?"at least ":""}${SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_1} more`:SYSTEM_REMINDER_DIR_SYNC_NAME_LIST_OVERFLOW_SUFFIX_VAR_2?" and more":""}
