<!--
name: Artifact Publish 408 Read Timeout
description: Deploy 408 tool result when the server stopped waiting for the upload.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_2
-->
deploy 408: ${TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_1(TOOL_RESULT_ARTIFACT_PUBLISH_408_READ_TIMEOUT_VAR_2,200),"Nothing was published; the server stopped waiting for the upload — retry once.")}
