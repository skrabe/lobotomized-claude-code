<!--
name: 'Artifact publish: unchecked hard link'
description: Publish error when a file is an unchecked hard link or was just replaced.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_ARTIFACT_FILES_UNCHECKED_HARD_LINK_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_UNCHECKED_HARD_LINK_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_UNCHECKED_HARD_LINK_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_UNCHECKED_HARD_LINK_VAR_1)} is an unchecked hard link, or was just replaced. Retry the publish, or publish a plain copy.
