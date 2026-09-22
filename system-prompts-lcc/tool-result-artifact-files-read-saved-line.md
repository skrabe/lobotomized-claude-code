<!--
name: Artifact Files-Read Saved Line
description: >-
  Per-file saved line in a files_read tool_result, with size, type, hash, and
  optional as-served note.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_3
-->
- ${TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_0(TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1.path,TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_2)} saved (${TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1.size_bytes} bytes, ${TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_3(TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1.content_type)}, sha256 ${TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1.sha256})${TOOL_RESULT_ARTIFACT_FILES_READ_SAVED_LINE_VAR_1.as_served?" exactly as served: the page could not be verified against the file listing, so it may include the service's runtime block":""}
