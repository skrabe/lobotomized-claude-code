<!--
name: 'Tool result: Artifact db as_level invalid'
description: Artifact read_db/write_db error listing the allowed as_level values.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_INVALID_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_INVALID_VAR_1
-->
as_level must be one of ${TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_INVALID_VAR_0.map((TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_INVALID_VAR_1)=>`'${TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_INVALID_VAR_1}'`).join(", ")}
