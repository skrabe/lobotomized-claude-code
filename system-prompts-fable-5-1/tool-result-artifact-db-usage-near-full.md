<!--
name: 'Tool Result: Artifact DB Usage Near Full'
description: >-
  write_db usage tail when the artifact database is at least 80% full, urging
  prune/aggregate instead of one document per item.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_0} It is ${TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_1.floor(TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_2*100/TOOL_RESULT_ARTIFACT_DB_USAGE_NEAR_FULL_VAR_3)}% full — prune or aggregate rather than creating one document per item.
