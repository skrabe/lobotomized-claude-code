<!--
name: Artifact files path starts with reserved underscore
description: >-
  Publish-time rejection when a files entry's path or top-level directory begins
  with "_", which the artifact service reserves.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_FILES_UNDERSCORE_RESERVED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_UNDERSCORE_RESERVED_VAR_1
-->
files: published path ${TOOL_RESULT_ARTIFACT_FILES_UNDERSCORE_RESERVED_VAR_0(TOOL_RESULT_ARTIFACT_FILES_UNDERSCORE_RESERVED_VAR_1)} starts with "_", which the artifact service reserves for its own names — rename the file or its top-level directory
