<!--
name: DirectoryAdded Hook Failed Notification
description: >-
  Task-notification line injected into the conversation after /add-dir when one
  or more DirectoryAdded hooks failed and their output was suppressed.
ccVersion: 2.1.219
variables:
  - DATA_TASK_NOTIFICATION_DIRECTORY_ADDED_HOOK_FAILED_VAR_0
  - DATA_TASK_NOTIFICATION_DIRECTORY_ADDED_HOOK_FAILED_VAR_1
-->
${DATA_TASK_NOTIFICATION_DIRECTORY_ADDED_HOOK_FAILED_VAR_0} DirectoryAdded ${DATA_TASK_NOTIFICATION_DIRECTORY_ADDED_HOOK_FAILED_VAR_1(DATA_TASK_NOTIFICATION_DIRECTORY_ADDED_HOOK_FAILED_VAR_0,"hook")} failed; output is in the debug log, not shown here
