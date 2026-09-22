<!--
name: Artifact Publish Update File Changes Refused
description: >-
  Tool result when the server rejects an update's file changes, leaving the
  artifact unchanged.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_3
-->
The server didn't accept this update's file changes (HTTP ${TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_0})${TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_1}. Nothing was published or removed; the artifact is unchanged. Publishing the page on its own (omitting \`files\`) would update the page but can't remove a file.${TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_2?.TOOL_RESULT_ARTIFACT_PUBLISH_UPDATE_FILE_CHANGES_REFUSED_VAR_3??""}
