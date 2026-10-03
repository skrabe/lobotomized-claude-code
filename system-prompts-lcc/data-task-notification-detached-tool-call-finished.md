<!--
name: 'Data: Task notification detached tool call finished'
description: >-
  Task-notification summary for a detached tool call that finished: its result
  follows, carry on as if the tool just returned, and do not re-answer a request
  the user dropped
ccVersion: 2.1.288
variables:
  - DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_0
  - DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_1
-->
The ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_0} call finished; its result follows. ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_CALL_FINISHED_VAR_1?"On the user's screen it just landed in that call's own row, like any tool result. ":""}Carry on from it as if the tool had just returned: do not announce a notification or a background task. If the user has since said they no longer need this result, do not answer the old request again: correct anything you got wrong in one or two lines, or say nothing new.
