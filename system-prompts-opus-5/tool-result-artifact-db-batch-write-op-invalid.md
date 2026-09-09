<!--
name: 'Tool Result: Artifact DB Batch Write Op Invalid'
description: >-
  validateInput rejection when a batch writes[i].op is missing or not one of
  set/update/delete.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_0}.op must be one of ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_1.map((TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2)=>`'${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_2}'`).join(", ")}${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_3.op===TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_OP_INVALID_VAR_4?" — str_replace is a single-document call, never a batch entry":""}.
