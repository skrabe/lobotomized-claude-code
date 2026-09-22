<!--
name: 'Tool Result: Artifact DB Batch Writes Too Many'
description: validateInput rejection when writes holds more entries than one batch accepts.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_TOO_MANY_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_TOO_MANY_VAR_1
-->
\`writes\` holds ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_TOO_MANY_VAR_0.length} entries — a batch takes at most ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITES_TOO_MANY_VAR_1}; split it across calls.
