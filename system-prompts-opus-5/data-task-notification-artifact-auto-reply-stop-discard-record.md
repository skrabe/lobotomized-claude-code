<!--
name: 'Data: Artifact Auto-Reply Stop Disclosure'
description: >-
  Discloses prior automatic artifact actions whose pending notice was discarded
  when watching stopped.
ccVersion: 2.1.228
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_1
-->
Before the stop, ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_0.family==="auto-edited"?`Artifact: ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_0.artifactName} had already been auto-edited in response to ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_1}`:`automatic replies had already been posted on ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_1} of Artifact: ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_DISCARD_RECORD_VAR_0.artifactName}`} (the pending notice was discarded with the stop — the artifact's thread and version history carry the record).
