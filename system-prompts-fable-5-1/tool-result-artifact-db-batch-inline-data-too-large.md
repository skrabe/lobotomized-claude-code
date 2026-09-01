<!--
name: 'Tool Result: Artifact DB Batch Inline Data Too Large'
description: >-
  validateInput rejection when the serialized inline data of writes[0..i]
  exceeds one batch request's byte cap.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_2
-->
the inline \`data\` of writes[0..${TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_0}] already serializes to ${TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_1} bytes — one batch request carries at most ${TOOL_RESULT_ARTIFACT_DB_BATCH_INLINE_DATA_TOO_LARGE_VAR_2}; split the batch across calls.
