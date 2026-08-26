<!--
name: 'Data: Task notification for re-armed artifact auto-replies'
description: >-
  Task notification telling the agent auto-replies on an artifact were resumed
  or re-enabled after a stop, naming which stop it was and how to disarm again.
ccVersion: 2.1.246
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_3
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_4
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_5
-->
Auto-replies on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0} were ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_1?"resumed by a resume_replies request":"re-enabled by this publish"} — they had been ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_2?"handed to another session of this conversation that resumed it or published there":DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_3?"paused when the user interrupted the session (Ctrl+C or Stop) and the watch had since dropped":"stopped when their live-updates task was killed"}. ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_3&&!DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_2?DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_4:DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_5}
