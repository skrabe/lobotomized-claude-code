<!--
name: 'Artifact auto-reply stopped on Esc: notification body'
description: >-
  Body wrapper of the task notification emitted when Esc stops artifact
  auto-reply subscriptions; carries the re-arm note.
ccVersion: 2.1.233
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_2
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_0(`A future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_ESC_STOPPED_BODY_VAR_2,"it","them")}, and an explicitly requested watch reconnects on its own without auto-reply; use the kill-all-agents gesture to disarm auto-replies for the whole session. Do not republish to re-enable auto-replies unless the user asks.`)}
