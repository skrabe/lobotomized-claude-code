<!--
name: 'Tool Result: Artifact DB Usage Full'
description: >-
  write_db usage tail when the artifact database is at its document cap, so
  creates will fail until rows are pruned.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ARTIFACT_DB_USAGE_FULL_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_USAGE_FULL_VAR_0} It is full: writes that create a document will fail until some are deleted — prune or aggregate existing documents.
