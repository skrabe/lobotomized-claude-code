<!--
name: 'Tool Result: db_read Not-Saved Line'
description: >-
  Per-reason line in the db_read saved tool_result listing returned documents
  that were not written under out_dir.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3
-->

[${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length} returned ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1(TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length,"document")} not saved — ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2[ue]}${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3}; read ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length===1?"it":"them"} without out_dir if needed]
