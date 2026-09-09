<!--
name: Artifact write_db new_str Exceeds Document Limit
description: validateInput error when new_str is larger than a document can hold.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_0
  - TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_1
  - TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_2
-->
\`new_str\` is ${TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_0.byteLength(TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_1,"utf8")} bytes of UTF-8 — a document holds at most ${TOOL_RESULT_ARTIFACT_WRITE_DB_NEW_STR_EXCEEDS_DOCUMENT_LIMIT_VAR_2}, so this edit can never fit.
