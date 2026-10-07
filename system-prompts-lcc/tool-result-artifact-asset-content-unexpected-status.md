<!--
name: 'Tool Result: Artifact asset content unexpected status'
description: >-
  Artifact asset read error for an unexpected HTTP status from the artifact
  service or content host.
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_CONTENT_UNEXPECTED_STATUS_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_CONTENT_UNEXPECTED_STATUS_VAR_1
-->
unexpected answer from the ${TOOL_RESULT_ARTIFACT_ASSET_CONTENT_UNEXPECTED_STATUS_VAR_0?"artifact service":"content host"} (HTTP ${TOOL_RESULT_ARTIFACT_ASSET_CONTENT_UNEXPECTED_STATUS_VAR_1.status})
