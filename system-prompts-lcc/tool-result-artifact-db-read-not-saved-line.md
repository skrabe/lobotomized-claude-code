<!--
name: Artifact DB Read Not Saved Line
description: >-
  Tells the model how many returned database documents were not saved and to
  read them without out_dir.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3
-->

[${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length} returned ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_1(TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length,"document")} not saved — ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_2[Y]}${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_3}; read ${TOOL_RESULT_ARTIFACT_DB_READ_NOT_SAVED_LINE_VAR_0.length===1?"it":"them"} without out_dir if needed]
