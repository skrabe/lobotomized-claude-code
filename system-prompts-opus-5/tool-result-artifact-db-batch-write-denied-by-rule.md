<!--
name: 'Tool Result: Artifact DB Batch Write Denied By Rule'
description: >-
  checkPermissions deny when a writes[i] entry matches a deny rule, so nothing
  in the batch was written.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_2
-->
Permission to use ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_0} with ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_1(TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_2.rule)} has been denied (writes[${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_DENIED_BY_RULE_VAR_2.index}] of this batch matches it), so nothing in the batch was written.
