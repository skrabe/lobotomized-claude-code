<!--
name: 'Data: Task notification for refused artifact auto-edit'
description: >-
  Task notification telling the agent an auto-reply was posted but the requested
  automatic artifact edit was refused, so the artifact is unchanged and the
  agent should make the change itself.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_REFUSED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_REFUSED_VAR_1
-->

Auto-reply posted to thread ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_REFUSED_VAR_0.id} on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_REFUSED_VAR_1}: a requested automatic edit was refused, so the artifact was NOT changed. Read the thread and make the change yourself if appropriate.
