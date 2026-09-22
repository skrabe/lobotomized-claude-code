<!--
name: 'Tool Result: Artifact DB Batch Collection/Doc Id Format'
description: >-
  validateInput rejection when a batch entry's collection/doc_id fail the
  1-15-segment path grammar.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_COLLECTION_DOC_ID_FORMAT_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_COLLECTION_DOC_ID_FORMAT_VAR_0} needs \`collection\` (a "/"-separated path of 1-15 segments) and \`doc_id\` (one segment) — letters, digits and _ - . ~ : @ + per segment, not "." or "..".
