<!--
name: 'Data: Task notification for re-armed artifact auto-replies'
description: >-
  Task notification telling the agent that publishing re-enabled auto-replies on
  an artifact whose live-updates task had been killed, and how to disarm them
  again.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0
-->

Auto-replies on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLIES_REARMED_VAR_0} were re-enabled by this publish — they had been stopped when their live-updates task was killed. If this wasn't intended, kill the task again to stop them for this artifact, or use the kill-all-agents gesture to disarm auto-replies for the whole session.
