<!--
name: 'Tool Parameter: Artifact db_op'
description: >-
  Artifact tool input-schema description of the `db_op` parameter selecting the
  read_db/write_db database operation.
ccVersion: 2.1.265
variables:
  - TOOL_PARAMETER_ARTIFACT_DB_OP_VAR_0
  - TOOL_PARAMETER_ARTIFACT_DB_OP_VAR_1
-->
'batch' to send up to ${TOOL_PARAMETER_ARTIFACT_DB_OP_VAR_1} ${TOOL_PARAMETER_ARTIFACT_DB_OP_VAR_0?"set/update/delete writes":"of those"} in `writes` under one approval. Required for both database actions; meaningless for every other action.
