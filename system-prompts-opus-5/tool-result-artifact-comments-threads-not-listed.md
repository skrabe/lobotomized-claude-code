<!--
name: Artifact Comments Threads Not Listed
description: >-
  Trailer row telling the model how many comment threads were omitted entirely
  from the tool_result because of the size cap; reworded from the 2.1.221 id of
  the same name to add the sent-to-Claude count.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_0
  - TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_1
  - TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_2
  - TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_3
-->
[${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_0} more ${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_1(TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_0,"thread")} not listed${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_2>0?` (${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_2} with ${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_1(TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_2,"comment")} sent to Claude)`:""} — size cap; ${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_3!==void 0?`re-run action "comments" with cursor "${TOOL_RESULT_ARTIFACT_COMMENTS_THREADS_NOT_LISTED_VAR_3}" to continue the list, or `:""}view them on the artifact page]
