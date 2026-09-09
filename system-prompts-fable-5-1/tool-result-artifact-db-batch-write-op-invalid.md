<!--
name: Artifact write_db Batch Op Invalid
description: >-
  validateInput error when a batch writes[i].op is missing or not an allowed
  batch op, with the str_replace-not-in-batch clause interpolated. (id reused:
  same validateInput rejection, 2.1.265 appends the
  str_replace-not-a-batch-entry clause)
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_3
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_4
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_0}.op must be one of ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_1.map((TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2)=>`'${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2}'`).join(", ")}${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_3.op===TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_4?" — str_replace is a single-document call, never a batch entry":""}.
