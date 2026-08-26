<!--
name: 'Tool Result: Artifact DB Batch Write Too Large'
description: >-
  Kbs too_large arm of an artifact_db_write batch error, thrown as
  ArtifactInputError so the model sees that the 1 MiB batch body was rejected
  and nothing was written.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_TOO_LARGE_VAR_1
-->
db batch write failed (${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_TOO_LARGE_VAR_0(TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_TOO_LARGE_VAR_1)}): the batch body exceeds the server's 1 MiB request limit — nothing was written; split it into smaller write_db calls
