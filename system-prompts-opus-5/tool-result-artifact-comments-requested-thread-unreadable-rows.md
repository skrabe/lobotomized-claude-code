<!--
name: Artifact comments — requested thread not among readable rows
description: >-
  tool_result text when the requested thread_id is not among the comment rows of
  the record that could be read, with the drop reasons and a retry instruction.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_REQUESTED_THREAD_UNREADABLE_ROWS_VAR_0
-->
The requested comment thread is not among the rows of this record that could be read (${TOOL_RESULT_ARTIFACT_COMMENTS_REQUESTED_THREAD_UNREADABLE_ROWS_VAR_0.join("; ")}) — run action "comments" with its thread_id again for a live read.
