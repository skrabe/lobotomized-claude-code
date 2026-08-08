<!--
name: 'Data: Artifact auto-edit patch-failed notification'
description: >-
  Task notification injected when an artifact comment auto-reply was posted but
  the requested automatic edit could not be applied to the artifact's current
  source.
ccVersion: 2.1.224
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_PATCH_FAILED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_PATCH_FAILED_VAR_1
-->
Auto-reply posted to thread ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_PATCH_FAILED_VAR_0.id} on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_PATCH_FAILED_VAR_1}: a requested automatic edit could not be applied to the artifact's current source, so the artifact was NOT changed. Read the thread and make the change yourself if appropriate.
