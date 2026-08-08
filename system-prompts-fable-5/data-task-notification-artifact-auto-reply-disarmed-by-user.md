<!--
name: 'Task Notification: Artifact Auto-Replies Disarmed By User'
description: >-
  Enqueued as a task notification when the user fires the kill-all-agents
  gesture with live artifact auto-reply subscriptions, telling the model the
  subscriptions were stopped and auto-replies stay disarmed for the rest of the
  session.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_DISARMED_BY_USER_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_DISARMED_BY_USER_VAR_1
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_DISARMED_BY_USER_VAR_0} artifact auto-reply ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_DISARMED_BY_USER_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_DISARMED_BY_USER_VAR_0,"subscription")} stopped by the user — auto-replies are disarmed for the rest of this session (a new session re-arms on publish).
