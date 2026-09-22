<!--
name: 'Tool Result: Artifact Durable Wake Status'
description: >-
  Current durable-wake watch status returned to the model with the artifact URL
  and status note.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_0
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_1
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_2
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_3
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_4
-->
${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_0}Durable wake subscription on ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_1(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_2.url)} — ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_3(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_2.note)??`this session will be woken by a new turn when the artifact is ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_4.isArray(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_2.events)&&TOOL_RESULT_ARTIFACT_DURABLE_WAKE_STATUS_VAR_2.events.includes("comment")?"republished or a comment on it is sent to Claude":"next published"}; no live updates are streamed, so re-read the artifact on wake.`}
