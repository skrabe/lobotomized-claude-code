<!--
name: 'Tool Result: Artifact Pin Relay HTTP Failed'
description: >-
  Artifact pin/unpin tool_result when the cloud relay returns a non-2xx HTTP
  status.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ARTIFACT_PIN_RELAY_HTTP_FAILED_VAR_0
  - TOOL_RESULT_ARTIFACT_PIN_RELAY_HTTP_FAILED_VAR_1
-->
Couldn't confirm the ${TOOL_RESULT_ARTIFACT_PIN_RELAY_HTTP_FAILED_VAR_0} (the cloud relay failed: HTTP ${TOOL_RESULT_ARTIFACT_PIN_RELAY_HTTP_FAILED_VAR_1.status}) — check with action "list" before retrying.
