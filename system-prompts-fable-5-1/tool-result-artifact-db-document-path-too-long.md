<!--
name: 'Tool Result: Artifact DB Document Path Too Long'
description: >-
  Artifact tool validateInput rejection returned to the model when the composed
  `collection`/`doc_id` path exceeds the byte cap.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_DOCUMENT_PATH_TOO_LONG_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_DOCUMENT_PATH_TOO_LONG_VAR_1
-->
the composed document path (\`collection\` plus \`doc_id\`) is ${TOOL_RESULT_ARTIFACT_DB_DOCUMENT_PATH_TOO_LONG_VAR_0.length} bytes — the limit is ${TOOL_RESULT_ARTIFACT_DB_DOCUMENT_PATH_TOO_LONG_VAR_1}.
