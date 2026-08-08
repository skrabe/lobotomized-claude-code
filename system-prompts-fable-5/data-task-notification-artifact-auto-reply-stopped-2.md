<!--
name: Artifact Auto-Reply Subscriptions Stopped
description: >-
  Value passed to
  `yd({…mode:"task-notification",origin:{source:"artifact-auto-react-stop-disclosure"}})`
  in q$o(); injected as a task notification telling the model that N artifact
  auto-reply subscriptions stopped and not to republish to re-enable them
  unprompted.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_1
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_0} artifact auto-reply ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_0,"subscription")} stopped — a future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOPPED_2_VAR_0,"it","them")}. Do not republish to re-enable auto-replies unless the user asks.
