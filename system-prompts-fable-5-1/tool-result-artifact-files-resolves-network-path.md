<!--
name: 'Tool Result: Artifact File Resolves To A Network Path'
description: >-
  Error returned to the model when a `files` source realpath resolves to a
  network path.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_2
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_1)} resolves to a network path — only files under ${TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_2} can be published
