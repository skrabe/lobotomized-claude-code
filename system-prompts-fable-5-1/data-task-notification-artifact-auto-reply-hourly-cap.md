<!--
name: 'Artifact Auto-Reply Paused: Hourly Cap'
description: >-
  notify() task-notification telling the model new artifact comments arrived but
  auto-reply hit its hourly cap, and to use the Artifact tool to read and reply
  manually.
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_HOURLY_CAP_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_HOURLY_CAP_VAR_1
-->
${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_HOURLY_CAP_VAR_0} — auto-reply held back (hourly cap); use ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_HOURLY_CAP_VAR_1()} to read and reply.
