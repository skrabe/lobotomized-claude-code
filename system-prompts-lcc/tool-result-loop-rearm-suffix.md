<!--
name: 'Tool Result: Loop Re-arm Suffix'
description: >-
  Model-facing tool_result sentence shared by both loop-stopped envelopes: if a
  wakeup tool was armed for this loop, trigger the stop tool now. Split out of
  tool-result-loop-stopped in 2.1.206.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_LOOP_REARM_MONITOR_TOOL
  - TOOL_RESULT_LOOP_REARM_TASKSTOP_TOOL
-->
If you armed a ${TOOL_RESULT_LOOP_REARM_MONITOR_TOOL} for this loop, ${TOOL_RESULT_LOOP_REARM_TASKSTOP_TOOL} it now; otherwise nothing more to do this turn.
