<!--
name: 'Tool Result: Artifact DB Quota Exceeded'
description: >-
  Artifact read_db/write_db error envelope for quota_exceeded, falling back to a
  storage-limit sentence.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_0}: ${TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_1(TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_2,TOOL_RESULT_ARTIFACT_DB_QUOTA_EXCEEDED_VAR_3)??"a storage limit on this artifact's database has been reached — delete documents; retrying won't help"}
