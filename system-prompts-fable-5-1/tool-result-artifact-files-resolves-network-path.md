<!--
name: 'Tool result: Artifact file resolves to a network path'
description: >-
  Error returned to the model when a `files` source resolves (via realpath) to a
  network path.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_RESOLVES_NETWORK_PATH_VAR_1)} resolves to a network path — only files under the working directory can be published
