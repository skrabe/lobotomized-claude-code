<!--
name: 'System Reminder: Directory sync nested repository not entered'
description: >-
  dir_sync_notice telling the model sync never enters a nested git repo so
  nothing inside it reaches the user's machine, and to tell the user if those
  files are needed.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_2
-->
Directory sync: ${SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_0} ${SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_1?"is a git repository of its own":"are git repositories of their own"} inside the project (nested); sync never enters a nested repository, so NOTHING inside ${SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_1?"it":"them"} reaches the user's machine (the user is told as well). If the user needs those files on their machine, tell them they exist only here${SYSTEM_REMINDER_DIR_SYNC_NESTED_REPOSITORY_NOT_ENTERED_VAR_2}.
