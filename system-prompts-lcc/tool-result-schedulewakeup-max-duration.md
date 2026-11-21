<!--
name: 'Tool result: ScheduleWakeup max duration'
description: >-
  Wakeup not scheduled because the loop reached its maximum duration; tell the
  user how to restart.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_SCHEDULEWAKEUP_MAX_DURATION_VAR_0
-->
Wakeup not scheduled. The loop reached its maximum duration — the loop has ended; do not re-issue. Tell the user that it has ended, and that after a minute they can start it again with the same /loop command; write that command out, prompt included. ${TOOL_RESULT_SCHEDULEWAKEUP_MAX_DURATION_VAR_0}
