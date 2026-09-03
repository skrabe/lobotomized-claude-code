<!--
name: 'Tool Result: Artifact files path contains backslash'
description: >-
  Validation error for the Artifact publish `files` map, returned to the model
  when a published path contains a backslash instead of forward slashes.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_2
-->
${TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_0} ${TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_PATH_BACKSLASH_VAR_2)} contains a backslash — published paths use forward slashes on every platform
