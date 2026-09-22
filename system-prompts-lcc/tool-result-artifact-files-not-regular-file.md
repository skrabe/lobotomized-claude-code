<!--
name: 'Tool result: Artifact file is not a regular file'
description: >-
  Error returned to the model when a `files` source is not a regular file (e.g.
  a directory, device, or FIFO).
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_NOT_REGULAR_FILE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_NOT_REGULAR_FILE_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_NOT_REGULAR_FILE_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_NOT_REGULAR_FILE_VAR_1)} is not a regular file
