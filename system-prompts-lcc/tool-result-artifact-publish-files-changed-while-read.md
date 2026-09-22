<!--
name: Artifact Publish Files Changed While Read
description: >-
  Publish validation error when a supporting file changed on disk while it was
  being read.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CHANGED_WHILE_READ_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CHANGED_WHILE_READ_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CHANGED_WHILE_READ_VAR_0.stringify(TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CHANGED_WHILE_READ_VAR_1)} changed while it was read — retry the publish
