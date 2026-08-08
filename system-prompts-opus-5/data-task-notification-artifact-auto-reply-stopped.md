<!--
name: 'Task Notification: Artifact Auto-Reply Subscription Stopped'
description: >-
  Queued via yd (Ly.enqueuePendingNotification) with mode:"task-notification"
  from qGs/q$o when artifact auto-react subscriptions are torn down; tells the
  model the auto-replies stopped, that a future publish re-arms them, and not to
  republish just to re-enable them.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_1
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_0} artifact auto-reply ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_0,"subscription")} stopped — a future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_VAR_0,"it","them")}; use the kill-all-agents gesture to disarm auto-replies for the whole session. Do not republish to re-enable auto-replies unless the user asks.
