<!--
name: 'Task notification: background tasks stopped over Remote Control'
description: >-
  Queued task-notification telling the model which background tasks the user
  stopped over Remote Control and not to restart them unless asked.
ccVersion: 2.1.326
variables:
  - DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_0
  - DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_1
  - DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_2
  - DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_3
-->
Background ${DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_0} stopped by the user over Remote Control: ${DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_1.join(", ")}. ${DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_2} no longer running and no result will follow. Do not start ${DATA_TASK_NOTIFICATION_REMOTE_CONTROL_BACKGROUND_TASKS_STOPPED_VAR_3} again unless the user asks.
