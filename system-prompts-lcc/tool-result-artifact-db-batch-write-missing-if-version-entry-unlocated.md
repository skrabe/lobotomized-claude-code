<!--
name: 'Tool Result: Artifact db batch write missing if_version (entry not located)'
description: >-
  Batch-write error returned when an unpinned write targeted an existing
  document and the tool cannot say which entry: read the documents this batch
  writes, pin if_version, resend.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_ENTRY_UNLOCATED_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_ENTRY_UNLOCATED_VAR_0}: one of the writes targets a document that already exists and carried no if_version — the whole batch wrote nothing. Read the existing documents this batch writes, re-plan those entries on what they hold now with if_version set to the versions the reads return, then resend the batch
