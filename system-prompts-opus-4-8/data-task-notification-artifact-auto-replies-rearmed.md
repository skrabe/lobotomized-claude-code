<!--
name: 'Data: Task notification for re-armed artifact auto-replies'
description: >-
  Task notification telling the agent that publishing re-enabled auto-replies on
  an artifact whose live-updates task had been killed, and how to disarm them
  again.
ccVersion: 2.1.234
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0
-->
Auto-replies on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0} were ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_1?"resumed by a resume_replies request":"re-enabled by this publish"} — they had been stopped when ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_2?"the user interrupted the session (Ctrl+C or Stop)":"their live-updates task was killed"}. ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_3}
