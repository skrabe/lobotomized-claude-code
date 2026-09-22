<!--
name: 'Data: Artifact Durable Wake — Not-Woken Condition'
description: >-
  Clause stating that the session will not be woken on republish or on a comment
  sent to Claude when the durable wake subscription did not register.
ccVersion: 2.1.238
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_DURABLE_WAKE_NOT_WOKEN_CONDITION_VAR_0
-->
This session will NOT be woken when ${DATA_TASK_NOTIFICATION_ARTIFACT_DURABLE_WAKE_NOT_WOKEN_CONDITION_VAR_0()?"it is republished or a comment on it is sent to Claude":"it is republished"}
