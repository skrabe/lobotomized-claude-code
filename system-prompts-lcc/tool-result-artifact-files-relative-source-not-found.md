<!--
name: 'Tool result: artifact relative source not found'
description: >-
  Artifact publish error explaining a relative files source is read from root or
  the working directory and how to give an absolute source.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_2
  - TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_3
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_1)} not found in ${TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_2(TOOL_RESULT_ARTIFACT_FILES_RELATIVE_SOURCE_NOT_FOUND_VAR_3)}. A relative source is read from that folder, which is \`root\` if given and otherwise the working directory, even when file_path is somewhere else. Give its path relative to that folder, or give its absolute path in the map form ({"published/path": "/absolute/source"}).
