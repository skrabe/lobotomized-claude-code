<!--
name: 'Tool Result: Artifact DB Write Committed'
description: >-
  Success line of the artifact write_db tool_result confirming the document was
  committed and that every viewer of the artifact sees the change.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2
-->
Database ${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_0(TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1.op)} committed: ${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2(TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1.collection)}/${TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_2(TOOL_RESULT_ARTIFACT_DB_WRITE_COMMITTED_VAR_1.doc_id)}.
