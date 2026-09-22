<!--
name: 'Tool Result: Artifact Pin Foreign Response'
description: >-
  Artifact pin/unpin tool_result when a relay 2xx body was not the Artifact
  service's own.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ARTIFACT_PIN_FOREIGN_RESPONSE_VAR_0
  - TOOL_RESULT_ARTIFACT_PIN_FOREIGN_RESPONSE_VAR_1
-->
Couldn't confirm the ${TOOL_RESULT_ARTIFACT_PIN_FOREIGN_RESPONSE_VAR_0}: the answer (HTTP ${TOOL_RESULT_ARTIFACT_PIN_FOREIGN_RESPONSE_VAR_1.status}) was not the Artifact service's own — check with action "list" before retrying.
