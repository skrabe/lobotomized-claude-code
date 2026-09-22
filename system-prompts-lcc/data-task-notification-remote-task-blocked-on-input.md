<!--
name: 'Data: Task notification remote task blocked on input'
description: >-
  Task-notification text stating a cloud session is waiting on input, with where
  to answer it or how to relaunch
ccVersion: 2.1.239
variables:
  - DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_INPUT_VAR_0
  - DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_INPUT_VAR_1
-->
the cloud session is waiting on input (a question, or a permission prompt this session couldn't answer for it). Answer it at ${DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_INPUT_VAR_0(DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_INPUT_VAR_1.sessionId)}, or relaunch with an agent whose permission mode doesn't prompt.
