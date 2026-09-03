<!--
name: 'System Reminder: Artifact editor follow-up failed or stopped'
description: >-
  Correction to the coordinator that the artifact editor read a follow-up but
  failed or was stopped, so it should not wait for that worker.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_FAILED_OR_STOPPED_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_FAILED_OR_STOPPED_VAR_1
-->
${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_FAILED_OR_STOPPED_VAR_0} read that follow-up but ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_FAILED_OR_STOPPED_VAR_1==="failed"?"failed":"was stopped"} before finishing. Do not wait for its result — if the page still needs that change, dispatch a new worker or answer directly.
