<!--
name: 'Tool result: Artifact file became a symlink after check'
description: >-
  TOCTOU error returned to the model when a `files` source changed to a symlink
  after it was validated.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_CHANGED_TO_SYMLINK_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_CHANGED_TO_SYMLINK_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_CHANGED_TO_SYMLINK_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_CHANGED_TO_SYMLINK_VAR_1)} changed to a symlink after it was checked — retry the publish
