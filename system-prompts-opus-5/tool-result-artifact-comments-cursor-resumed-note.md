<!--
name: Artifact Comments Cursor Resumed Note
description: >-
  Comments tool-result note reporting how many threads were skipped when
  resuming from a cursor and how the model can request the complete list.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_1
-->
 Resumed from the cursor: the ${TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_0} ${TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_1(TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_0,"thread")} at or before it in list order ${TOOL_RESULT_ARTIFACT_COMMENTS_CURSOR_RESUMED_NOTE_VAR_0===1?"is":"are"} skipped — threads enter or re-rank to the top as new comments arrive, so the skipped span can hold threads this walk never listed; re-run without \`cursor\` for the full list.
