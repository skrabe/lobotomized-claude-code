<!--
name: 'Tool Result: Artifact DB Version Mismatch'
description: >-
  Artifact write error when the document is no longer at the pinned version;
  nothing was written and the model must re-read and pin the current version.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_0}: the document is no longer at version ${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1?.TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_2??"?"}, the one this write was pinned to${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1?.TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_3!==void 0?` — it is now at version ${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1.current}`:""}; nothing was written. Read it back, re-plan the edit against what it holds now, and pin to that version
