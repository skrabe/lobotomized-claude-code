<!--
name: 'Tool Result: Artifact Watch Backing Off'
description: >-
  Artifact status tool-result row for a watch that is not connected and is
  waiting to reconnect, including retry timing and failure cap.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_2
-->
- ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_0} — not connected: the next reconnect attempt is in about ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1.next_in_s??"?"}s (as of this status)${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_2}; it gives up after more than ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1.max_failures??"?"} consecutive failures, retries on its own until then, and you are told if it has to stop.
