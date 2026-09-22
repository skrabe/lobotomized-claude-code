<!--
name: 'Data: Task notification for artifact auto-edit with unknown outcome'
description: >-
  Task-notification detail telling the agent an auto-edit reply was posted but
  the publish outcome is UNKNOWN, so the artifact and thread need review.
ccVersion: 2.1.234
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_VAR_1
-->
Auto-reply posted to thread ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_VAR_0.id} on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_VAR_1}: an automatic edit attempt could not confirm whether its publish landed, so it is UNKNOWN whether the artifact was changed. Review the artifact and the thread.
