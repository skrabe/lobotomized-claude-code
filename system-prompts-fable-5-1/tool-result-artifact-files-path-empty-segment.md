<!--
name: 'Artifact files: published path has an empty segment'
description: >-
  Path-validation tool-error returned to the model when a published path
  contains an empty segment (a doubled slash). New in CC 2.1.239 — it replaces
  the 2.1.238 whole-path-empty check, which is gone from the bundle.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_2
-->
${TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_0} ${TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_PATH_EMPTY_SEGMENT_VAR_2)} has an empty path segment
