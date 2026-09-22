<!--
name: 'Tool result: Artifact files param — absolute path needs map form'
description: >-
  Validation error when a files list entry is an absolute path; tells the model
  to use the published-path map form.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_0(TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_1.path)} is absolute — absolute sources need the map form ({"published/path": "source"}), which names the published path explicitly
