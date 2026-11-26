<!--
name: Subagent stalled error
description: >-
  Failure error/summary reported as the Task subagent result to the parent model
  when the stream watchdog detects a stall.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_SUBAGENT_STALLED_VAR_0
  - TOOL_RESULT_SUBAGENT_STALLED_VAR_1
-->
Agent stalled: no progress for ${TOOL_RESULT_SUBAGENT_STALLED_VAR_0.round(TOOL_RESULT_SUBAGENT_STALLED_VAR_1/1000)}s (stream watchdog did not recover)
