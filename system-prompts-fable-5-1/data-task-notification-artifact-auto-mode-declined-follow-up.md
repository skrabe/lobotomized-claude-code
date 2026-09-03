<!--
name: 'Data: Task Notification Artifact Auto Mode Declined Follow-Up'
description: >-
  Task-notification body when auto mode declined an unattended follow-up reply
  after this session already acknowledged the thread.
ccVersion: 2.1.246
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_MODE_DECLINED_FOLLOW_UP_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_MODE_DECLINED_FOLLOW_UP_VAR_1
-->
${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_MODE_DECLINED_FOLLOW_UP_VAR_0}. Auto mode did not approve the unattended follow-up reply, so it was not posted — only this session's acknowledgement${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_MODE_DECLINED_FOLLOW_UP_VAR_1.note}, which promised a reply, stands in the thread. Read the thread when ready and post the promised reply with acknowledge_duplicate: true (the duplicate guard refuses a plain follow-up). Further comments will not repeat this notice.
