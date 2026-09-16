<!--
name: 'Tool Result: Artifact asset relay unavailable'
description: >-
  Explains that the permission check passed but this environment cannot reach
  the content host directly, so reads go through the gateway.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_1.status)}. Your access to the artifact itself is fine (the permission check passed); this environment cannot reach ${TOOL_RESULT_ARTIFACT_ASSET_RELAY_UNAVAILABLE_VAR_2} directly, so its reads go through the gateway.
