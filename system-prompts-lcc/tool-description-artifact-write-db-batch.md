<!--
name: 'Tool Description: Artifact write_db Batch'
description: >-
  Dynamic write_db description lead when the call is a multi-document batch,
  including the host atomicity note from OBt().
ccVersion: 2.1.246
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_3
-->
Write ${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_0.length} ${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_1(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_0.length,"document")}${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_2?" (some from local JSON files)":""} to a published artifact's database in one batch, ${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_BATCH_VAR_3()}
