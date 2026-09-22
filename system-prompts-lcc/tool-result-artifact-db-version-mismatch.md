<!--
name: 'Tool Result: Artifact Db Write Version Mismatch'
description: >-
  write_db error when an if_version pin is stale and the server reports the
  document's current version.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_0}: the document is no longer at version ${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1.pinned??"?"}, the one this write was pinned to — it is now at version ${TOOL_RESULT_ARTIFACT_DB_VERSION_MISMATCH_VAR_1.current}; nothing was written. Read it back, re-plan the write against what it holds now, and pin to that version
