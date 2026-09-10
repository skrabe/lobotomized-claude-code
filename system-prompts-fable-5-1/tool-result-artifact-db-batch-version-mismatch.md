<!--
name: 'Tool Result: Artifact Db Batch Version Mismatch'
description: >-
  Atomic batch write_db error when a pinned if_version is stale and the server
  did not name which entry.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_VERSION_MISMATCH_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_VERSION_MISMATCH_VAR_0}. A document one of the writes was pinned to with if_version is no longer at that version (or no longer exists). Re-read the pinned documents, re-plan those writes against what they hold now with fresh pins, then resend the batch
