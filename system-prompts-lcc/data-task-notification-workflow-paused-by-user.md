<!--
name: 'Task notification: workflow paused by user'
description: >-
  Task notification body saying a paused workflow task is not running until
  resumed from /workflows.
ccVersion: 2.1.322
variables:
  - DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_0
  - DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_1
  - DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_2
-->

<${DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_0}>It is not running, and no result follows until it is resumed. The user can resume it from /workflows.</${DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_0}>${DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_1(DATA_TASK_NOTIFICATION_WORKFLOW_PAUSED_BY_USER_VAR_2)}
