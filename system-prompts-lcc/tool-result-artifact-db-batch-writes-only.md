<!--
name: 'Tool result: Artifact db batch op takes writes only'
description: >-
  Artifact write_db batch error when top-level document fields are passed
  alongside writes.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_ONLY_VAR_0
-->
db_op "${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_ONLY_VAR_0}" takes its documents in \`writes\` only — top-level collection, doc_id, data, file_path, if_version, and query are not accepted
