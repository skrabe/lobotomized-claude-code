<!--
name: 'Tool Result: Artifact File Source Is A Network Path'
description: >-
  Error returned to the model when a `files` source path points at a network
  location.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_2
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_1)} is a network path — only files under ${TOOL_RESULT_ARTIFACT_FILES_NETWORK_PATH_VAR_2} can be published
