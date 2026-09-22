<!--
name: 'Tool Result: Artifact DB Cursor Past Elided Documents'
description: >-
  Trailer used when the read_db tool_result had documents elided by the size
  cap, warning the model that the cursor skips past them unless query.limit is
  lowered.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_PAST_ELIDED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_PAST_ELIDED_VAR_1
-->

next_cursor: ${TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_PAST_ELIDED_VAR_0(TOOL_RESULT_ARTIFACT_DB_NEXT_CURSOR_PAST_ELIDED_VAR_1)} — this cursor continues past the elided documents; re-run with a smaller \`query.limit\` before paging on, or the elided documents are skipped.
