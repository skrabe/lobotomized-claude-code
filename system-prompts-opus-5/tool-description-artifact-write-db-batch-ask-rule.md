<!--
name: 'Tool Description: Artifact write_db Batch Ask Rule'
description: >-
  write_db description clause when writes[i] matches an ask rule, so this batch
  asks on its own and approval covers only it.
ccVersion: 2.1.246
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_2
-->
writes[${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0.index}] matches your ask rule ${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_1}(${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_2(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_ASK_RULE_VAR_0.rule)}), so this batch asks on its own and approving covers only it
