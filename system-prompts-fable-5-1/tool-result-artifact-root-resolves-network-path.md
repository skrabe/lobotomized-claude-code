<!--
name: 'Tool Result: Artifact root resolves to a network path'
description: >-
  Validation error for the Artifact publish `root` base directory, returned to
  the model when root's realpath resolves to a network path outside the working
  directory.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_1
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_NETWORK_PATH_VAR_1)} resolves to a network path — the publish base must lie within the working directory
