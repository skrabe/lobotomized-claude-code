<!--
name: 'Tool Result: Artifact DB Read Not Saved Line'
description: >-
  Line in a read_db out_dir result that lists returned documents that were not
  saved and why, with a hint to read them without out_dir.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3
-->

[${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length} returned ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1(TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length,"document")} not saved — ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2[te]}${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3}; read ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length===1?"it":"them"} without out_dir if needed]
