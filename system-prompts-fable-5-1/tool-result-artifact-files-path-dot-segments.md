<!--
name: 'Tool Result: Artifact files path has dot segments'
description: >-
  Validation error for the Artifact publish `files` map, returned to the model
  when a published path contains '.' or '..' segments.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILES_PATH_DOT_SEGMENTS_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_PATH_DOT_SEGMENTS_VAR_1
-->
${TOOL_RESULT_ARTIFACT_FILES_PATH_DOT_SEGMENTS_VAR_0} ${TOOL_RESULT_ARTIFACT_FILES_PATH_DOT_SEGMENTS_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_PATH_DOT_SEGMENTS_VAR_2)} contains "." or ".." segments — pass the plain served path
