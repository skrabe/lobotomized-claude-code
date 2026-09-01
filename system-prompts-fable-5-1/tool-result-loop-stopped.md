<!--
name: 'Tool Result: Loop Stopped'
description: >-
  Model-facing tool_result telling the model the dynamic loop stopped, with the
  wakeup-cancellation reason interpolated and the shared re-arm suffix appended.
  2.1.206 reduced this to an envelope (fuzzy-miss restore).
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_LOOP_STOPPED_REASON
  - TOOL_RESULT_LOOP_STOPPED_REARM_SUFFIX
-->
Loop stopped — ${TOOL_RESULT_LOOP_STOPPED_REASON}. ${TOOL_RESULT_LOOP_STOPPED_REARM_SUFFIX}
