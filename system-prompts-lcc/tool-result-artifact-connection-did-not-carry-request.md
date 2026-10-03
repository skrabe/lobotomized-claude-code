<!--
name: 'Tool Result: Artifact Connection Did Not Carry Request'
description: >-
  Artifact tool error detail saying the artifact connection did not carry the
  request, so nothing was sent, optionally noting one retry is safe.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ARTIFACT_CONNECTION_DID_NOT_CARRY_REQUEST_VAR_0
  - TOOL_RESULT_ARTIFACT_CONNECTION_DID_NOT_CARRY_REQUEST_VAR_1
-->
its artifact connection did not carry the request${TOOL_RESULT_ARTIFACT_CONNECTION_DID_NOT_CARRY_REQUEST_VAR_0?` (HTTP ${TOOL_RESULT_ARTIFACT_CONNECTION_DID_NOT_CARRY_REQUEST_VAR_0})`:""}, so nothing was sent${TOOL_RESULT_ARTIFACT_CONNECTION_DID_NOT_CARRY_REQUEST_VAR_1==="relay-unavailable"?"; one retry is safe":""}
