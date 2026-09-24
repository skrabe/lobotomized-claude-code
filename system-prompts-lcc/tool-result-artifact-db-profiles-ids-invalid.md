<!--
name: 'Tool Result: Artifact db profiles ids invalid'
description: >-
  Validation error telling the model the profiles db_op needs 1-N ids, each "u_"
  plus 22 characters, copied exactly from a document or live event.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_INVALID_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_INVALID_VAR_1
-->
db_op "${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_INVALID_VAR_0}" requires \`ids\`: 1-${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_INVALID_VAR_1} ids, each "u_" plus 22 letters, digits or underscores, exactly as a document or live event showed it.
