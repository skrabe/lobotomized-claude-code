<!--
name: 'Tool result: Artifact file source is a network path'
description: >-
  Error returned to the model when a `files` source path points at a network
  location (UNC/network mount).
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_1)} is a network path — only files under the working directory can be published
