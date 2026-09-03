<!--
name: 'Tool Result: Artifact DB Batch Too Large'
description: >-
  Batch write_db error when the serialized batch exceeds the per-request byte
  limit.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_TOO_LARGE_VAR_1
-->
the batch serializes to ${TOOL_RESULT_ARTIFACT_DB_BATCH_TOO_LARGE_VAR_0} bytes — the limit for one request is ${TOOL_RESULT_ARTIFACT_DB_BATCH_TOO_LARGE_VAR_1}; split it into smaller batches
