<!--
name: Artifact DB Read Not-Saved Line
description: >-
  read_db tool-result line listing returned documents that were not saved to
  out_dir, with the skip reason.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3
-->

[${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length} returned ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1(TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length,"document")} not saved — ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2[Ue]}${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3}; read ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length===1?"it":"them"} without out_dir if needed]
