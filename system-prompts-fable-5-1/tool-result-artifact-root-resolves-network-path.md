<!--
name: 'Tool Result: Artifact Root Resolves To A Network Path'
description: >-
  Validation error for Artifact publish `root` when realpath resolves to a
  network path.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_2
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_1)} resolves to a network path — the publish base must lie within ${TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_2}
