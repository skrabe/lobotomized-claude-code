<!--
name: 'Tool result: Artifact file path outside working directory'
description: >-
  Error returned to the model when an absolute `files` source path lies outside
  the working directory.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_VAR_1)} is outside the working directory — pass a path under it
