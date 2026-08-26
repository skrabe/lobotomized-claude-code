<!--
name: 'Tool Result: Artifact DB Batch Duplicate Path'
description: >-
  Batch write_db error when two ops in the same batch address the same document
  path.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_2
-->
write ${TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_0+1} of ${TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_1.length} addresses ${TOOL_RESULT_ARTIFACT_DB_BATCH_DUPLICATE_PATH_VAR_2.path}, which an earlier write in this batch already addresses — a batch writes each document at most once
