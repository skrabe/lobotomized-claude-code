<!--
name: Artifact Check Tool Prompt
description: >-
  Opens the artifact check tool prompt, telling the model when to check a page
  relative to publishing.
ccVersion: 2.1.280
variables:
  - TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_1
-->
Check a page ${TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_0.previewOn&&TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_0.verifyOn?"before or after":TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_0.previewOn?"before":"after"} publishing it with the \`${TOOL_DESCRIPTION_ARTIFACT_CHECK_VAR_1}\` tool.
