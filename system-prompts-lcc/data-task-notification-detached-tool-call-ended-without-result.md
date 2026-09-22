<!--
name: 'Task Notification: Detached Tool Call Ended Without Result'
description: >-
  Summary header of the task-notification for a detached tool call that failed
  or was stopped, telling the model to carry on as if the tool had returned and
  not to announce a notification.
ccVersion: 2.1.277
variables:
  - DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_ENDED_WITHOUT_RESULT_VAR_0
-->
The ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_ENDED_WITHOUT_RESULT_VAR_0} call ended without a result; what happened follows. On the user's screen that call's own row shows how it ended, like any tool error or interrupted call. Carry on as if the tool had just returned it: do not announce a notification or a background task.
