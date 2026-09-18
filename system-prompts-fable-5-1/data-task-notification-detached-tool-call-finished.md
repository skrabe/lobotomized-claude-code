<!--
name: 'Data: Task Notification Detached Tool Call Finished'
description: >-
  Task-notification summary when a detached tool call completes: its result
  follows, carry on as if the tool had just returned, do not announce a
  notification, and do not re-answer a request the user has since dropped.
ccVersion: 2.1.277
variables:
  - DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_0
-->
The ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_0} call finished; its result follows. On the user's screen it just landed in that call's own row, like any tool result. Carry on from it as if the tool had just returned: do not announce a notification or a background task. If the user has since said they no longer need this result, do not answer the old request again: correct anything you got wrong in one or two lines, or say nothing new.
