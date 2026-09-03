<!--
name: Artifact DB Batch Write Deny Rule
description: >-
  checkPermissions deny message when a batch write matches a deny rule, so
  nothing in the batch was written.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_2
-->
Permission to use ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_0} has been denied by your rule ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_1(TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_2.rule)} (writes[${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENY_RULE_VAR_2.index}] of this batch matches it), so nothing in the batch was written.
