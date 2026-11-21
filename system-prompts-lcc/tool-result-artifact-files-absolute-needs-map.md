<!--
name: 'Tool result: Artifact files param — absolute path needs map form'
description: >-
  Validation error for an absolute source path in the Artifact tool's `files`
  list, returned to the model as the tool's error result.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_0(TOOL_RESULT_ARTIFACT_FILES_ABSOLUTE_NEEDS_MAP_VAR_1.path)} is absolute — absolute sources need the map form ({"published/path": "source"}), which names the published path explicitly. The source must also lie under one of the session's working directories, or your scratchpad directory if you have one.
