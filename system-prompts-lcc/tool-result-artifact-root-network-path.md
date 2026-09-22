<!--
name: 'Tool Result: Artifact Root Is A Network Path'
description: >-
  Validation error for Artifact publish `root` when the given root is a network
  path.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_2
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_1)} is a network path — the publish base must lie within ${TOOL_RESULT_ARTIFACT_ROOT_NETWORK_PATH_VAR_2}
