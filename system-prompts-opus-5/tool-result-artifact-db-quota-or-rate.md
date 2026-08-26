<!--
name: 'Tool Result: Artifact DB Quota Or Rate'
description: >-
  Artifact read_db/write_db error envelope for quota_or_rate, falling back to a
  retry-later rate/storage limit sentence.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_0}: ${TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_1(TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_2,TOOL_RESULT_ARTIFACT_DB_QUOTA_OR_RATE_VAR_3)??"over a rate or storage limit — retry later or write less"}
