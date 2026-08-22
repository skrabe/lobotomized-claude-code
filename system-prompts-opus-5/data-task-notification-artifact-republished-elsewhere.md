<!--
name: 'Data: Artifact republished elsewhere notification'
description: >-
  Notification detail telling the model the artifact was republished by another
  session or saved from the page itself, that its copy is stale, and to re-read
  before editing or republishing
ccVersion: 2.1.239
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_2
-->
Artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_0} appears to have been republished elsewhere (by another session, or by someone saving from the page itself) — it is now version ${DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_1}. Your copy is stale; re-read before editing or republishing (${DATA_TASK_NOTIFICATION_ARTIFACT_REPUBLISHED_ELSEWHERE_VAR_2()}).
