<!--
name: 'Data: Artifact Notices Omitted'
description: >-
  Tells the model when earlier coalesced artifact notices were omitted from a
  notification burst.
ccVersion: 2.1.228
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_NOTICES_OMITTED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_NOTICES_OMITTED_VAR_1
-->


(${DATA_TASK_NOTIFICATION_ARTIFACT_NOTICES_OMITTED_VAR_0.droppedDetails} earlier ${DATA_TASK_NOTIFICATION_ARTIFACT_NOTICES_OMITTED_VAR_0.droppedDetails===1?"notice":"notices"} in this burst omitted — newest ${DATA_TASK_NOTIFICATION_ARTIFACT_NOTICES_OMITTED_VAR_1} kept.)
