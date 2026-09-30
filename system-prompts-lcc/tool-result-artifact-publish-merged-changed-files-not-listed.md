<!--
name: >-
  Tool Result: Artifact publish merge note when changed files could not be
  listed
description: >-
  Follow-on to the merged-over-newer-version note when the files that changed
  could not be listed, telling the model to re-read any copy it holds before
  editing or building on it
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MERGED_CHANGED_FILES_NOT_LISTED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MERGED_CHANGED_FILES_NOT_LISTED_VAR_1
-->


${TOOL_RESULT_ARTIFACT_PUBLISH_MERGED_CHANGED_FILES_NOT_LISTED_VAR_0} The files that changed there could not be listed: ${TOOL_RESULT_ARTIFACT_PUBLISH_MERGED_CHANGED_FILES_NOT_LISTED_VAR_1.listFiles!==void 0?`list them (${TOOL_RESULT_ARTIFACT_PUBLISH_MERGED_CHANGED_FILES_NOT_LISTED_VAR_1.listFiles}) and `:""}read again any file of this artifact you hold a copy of before you edit or build on it.
