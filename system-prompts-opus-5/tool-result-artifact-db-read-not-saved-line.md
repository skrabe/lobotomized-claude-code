<!--
name: Artifact Db Read Not Saved Line
description: >-
  Tool-result line listing returned artifact-db documents that were not written
  to out_dir, with the reason and ids.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3
-->

[${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length} returned ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1(TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length,"document")} not saved — ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2[he]}${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3}; read ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length===1?"it":"them"} without out_dir if needed]
