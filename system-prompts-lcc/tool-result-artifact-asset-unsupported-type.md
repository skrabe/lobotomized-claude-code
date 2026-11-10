<!--
name: 'Tool Result: Artifact asset unsupported content type'
description: 'Asset upload failed: server/intermediary refused the content type'
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UNSUPPORTED_TYPE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UNSUPPORTED_TYPE_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_UNSUPPORTED_TYPE_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_UNSUPPORTED_TYPE_VAR_1??"the server or an intermediary on this path refused the content type, which this client supports — a retry will not help"}
