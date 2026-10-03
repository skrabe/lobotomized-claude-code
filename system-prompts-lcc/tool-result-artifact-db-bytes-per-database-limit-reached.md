<!--
name: 'Tool Result: Artifact DB Bytes Per Database Limit Reached'
description: >-
  Artifact database refusal reason for bytes_per_database: the total document
  size limit is reached; delete documents or shrink them, and a larger rewrite
  of an existing document can also be refused.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ARTIFACT_DB_BYTES_PER_DATABASE_LIMIT_REACHED_VAR_0
-->
this artifact's database has reached its ${TOOL_RESULT_ARTIFACT_DB_BYTES_PER_DATABASE_LIMIT_REACHED_VAR_0} (the total size of its documents, not their count) — delete documents or make them smaller; a write that makes an existing document larger can be refused too, and retrying won't help
