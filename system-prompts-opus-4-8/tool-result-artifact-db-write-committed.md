<!--
name: 'Tool Result: Artifact DB Write Committed'
description: >-
  Success line of the artifact write_db tool_result confirming the document was
  committed and that every viewer of the artifact sees the change.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2
-->
Database ${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_0} committed: ${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1(TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2.collection)}/${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1(TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2.doc_id)}.
