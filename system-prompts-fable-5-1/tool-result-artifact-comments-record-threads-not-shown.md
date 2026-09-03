<!--
name: Artifact comments — record threads not shown
description: >-
  Truncation clause in the comments tool_result stating how many more threads of
  the record are not shown and how to get the live list.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_0
  - TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_1
-->
 ${TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_0} more ${TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_1(TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_0,"thread")} of this record ${TOOL_RESULT_ARTIFACT_COMMENTS_RECORD_THREADS_NOT_SHOWN_VAR_0===1?"is":"are"} not shown — run action "comments" again for the live list.
