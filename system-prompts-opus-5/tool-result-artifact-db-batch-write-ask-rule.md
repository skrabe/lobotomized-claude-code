<!--
name: 'Tool Result: Artifact DB Batch Write Ask Rule'
description: >-
  checkPermissions ask when writes[i] matches an ask rule and the full check
  could not complete, so approval covers only this call.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_2
-->
Claude wants to write a batch to this artifact's database, and writes[${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_0.index}] matches your ask rule ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_1}(${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_2(TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_ASK_RULE_VAR_0.rule)}) — the full permission check could not complete, so approving covers only this call.
