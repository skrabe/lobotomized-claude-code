<!--
name: 'Tool Result: Artifact Durable Wake Status'
description: >-
  Returned to the model with the current durable wake subscription status for an
  artifact.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_0
-->
Durable wake subscription on ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_0.url} — ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_0.note??"this session will be woken by a new turn when the artifact is next published; no live updates are streamed, so re-read the artifact on wake."}
