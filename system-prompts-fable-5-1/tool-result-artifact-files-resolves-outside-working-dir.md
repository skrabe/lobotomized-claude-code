<!--
name: 'Tool Result: Artifact File Resolves Outside Publish Base'
description: >-
  Validation error returned to the model when a `files` source realpath resolves
  outside the publish base, possibly via a symlink.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_2
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_1)} resolves outside ${TOOL_RESULT_ARTIFACT_FILES_RESOLVES_OUTSIDE_WORKING_DIR_VAR_2} (symlink?) — only files under it can be published
