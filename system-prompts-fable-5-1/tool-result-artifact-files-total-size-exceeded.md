<!--
name: 'Tool Result: Artifact Files Total Size Exceeded'
description: >-
  Artifact multi-file publish error returned to the model when the combined size
  of all files in a version exceeds the per-version limit.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_2
-->
files: total content exceeds ${TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_0/1024/1024}MB at ${TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_TOTAL_SIZE_EXCEEDED_VAR_2)} — a version's files may total at most that
