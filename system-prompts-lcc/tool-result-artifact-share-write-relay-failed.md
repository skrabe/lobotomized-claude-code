<!--
name: 'Artifact Share: Write Relay Failed'
description: >-
  Artifact share tool error when the cloud relay failed with an HTTP status on
  the share write; it may have gone through, so Claude must read the artifact
  first.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_WRITE_RELAY_FAILED_VAR_0
-->
Couldn't confirm the share (the cloud relay failed: HTTP ${TOOL_RESULT_ARTIFACT_SHARE_WRITE_RELAY_FAILED_VAR_0.status}) — it may have gone through; read the artifact before telling the person or trying again.
