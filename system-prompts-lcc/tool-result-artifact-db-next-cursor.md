<!--
name: 'Tool Result: Artifact DB Next Cursor'
description: >-
  Trailer appended to the artifact read_db tool_result handing the model the
  continuation cursor for the next page of documents.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_VAR_1
-->

next_cursor: ${TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_VAR_0(TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_VAR_1)} — more documents exist; pass this as \`query.cursor\` to read the next page.
