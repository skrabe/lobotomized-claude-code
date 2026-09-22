<!--
name: 'Tool Result: Artifact DB Data Too Large'
description: >-
  Artifact tool validateInput rejection returned to the model when the
  serialized `data` object exceeds the per-document UTF-8 byte cap.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_DATA_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_DATA_TOO_LARGE_VAR_1
-->
\`data\` serializes to ${TOOL_RESULT_ARTIFACT_DB_DATA_TOO_LARGE_VAR_0} bytes of UTF-8 — the limit is ${TOOL_RESULT_ARTIFACT_DB_DATA_TOO_LARGE_VAR_1}.
