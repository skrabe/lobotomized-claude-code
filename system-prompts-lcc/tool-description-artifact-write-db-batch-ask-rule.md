<!--
name: Artifact Write DB Batch Ask Rule
description: >-
  write_db description clause that a batch matching an ask rule asks on its own
  and approval covers only that call.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_1
-->
writes[${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0.index}] matches your ask rule ${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_1(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0.rule)}, so this batch asks on its own and approving covers only it
