<!--
name: 'Tool Result: Artifact DB write upload before writing more'
description: >-
  Tells Claude to upload each embedded file and write the returned id over the
  offending string(s) before writing more.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_0} Before writing more, upload each file ${TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_1} and write the id it returns over ${TOOL_RESULT_ARTIFACT_DB_WRITE_UPLOAD_BEFORE_WRITING_MORE_VAR_2===1?"that string; it stays":"each of those strings; they stay"} in the database until overwritten or deleted.
