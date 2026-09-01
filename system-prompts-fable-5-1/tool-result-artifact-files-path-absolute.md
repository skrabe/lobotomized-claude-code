<!--
name: 'Tool Result: Artifact files path is absolute'
description: >-
  Validation error for the Artifact publish `files` map, returned to the model
  when a published path is absolute rather than relative to the artifact root.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_1
-->
${TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_0} ${TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_2)} is absolute — published paths are relative to the artifact root
