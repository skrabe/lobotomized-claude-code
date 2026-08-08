<!--
name: 'Tool Result: Artifact DB doc_id Not Accepted'
description: >-
  Artifact tool validateInput rejection returned to the model when `doc_id` is
  passed with a collection-addressing db_op (query/list).
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_DOC_ID_NOT_ACCEPTED_VAR_0
-->
\`doc_id\` is not accepted with db_op "${TOOL_RESULT_ARTIFACT_DB_DOC_ID_NOT_ACCEPTED_VAR_0}" — it addresses a collection; use db_op "get" to read one document.
