<!--
name: Artifact watch status — backing off
description: >-
  Status-row line reporting the live watch is disconnected and backing off
  before its next reconnect attempt.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_3
-->
- ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_0} — not connected: the next reconnect attempt is in about ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_2.next_in_s)}s (as of this status)${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_3}; it gives up after more than ${TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_BACKING_OFF_VAR_2.max_failures)} consecutive failures, retries on its own until then, and you are told if it has to stop.
