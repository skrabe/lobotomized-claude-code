<!--
name: 'Data: Task Notification Artifact Source Owned No Auto Reply'
description: >-
  Wake notice that no auto-reply or auto-edit ran because this session publishes
  the artifact from source, so changes belong there.
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_3
-->
${DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_0}. No automatic reply was posted and no automatic edit was attempted: this session publishes the artifact from ${DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_1}, so a requested change belongs in that source (or whatever generates it), not in the served copy. Read the thread (${DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_2('Artifact tool, action "comments"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_SOURCE_OWNED_NO_AUTO_REPLY_VAR_3("comments"))}); answer any question in your reply, and if it asks for a change and the change is appropriate, make it in the source and republish.
