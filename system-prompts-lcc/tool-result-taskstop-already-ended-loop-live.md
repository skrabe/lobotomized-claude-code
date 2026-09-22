<!--
name: 'Tool Result: TaskStop Already Ended Loop Live'
description: >-
  TaskStop result note when the task had already ended but its loop was still
  live, so process groups were re-signalled.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_TASKSTOP_ALREADY_ENDED_LOOP_LIVE_VAR_0
  - TOOL_RESULT_TASKSTOP_ALREADY_ENDED_LOOP_LIVE_VAR_1
-->
had already ended (${TOOL_RESULT_TASKSTOP_ALREADY_ENDED_LOOP_LIVE_VAR_0.status}) but its loop had not exited; re-signalled it and killed ${TOOL_RESULT_TASKSTOP_ALREADY_ENDED_LOOP_LIVE_VAR_1} process group(s). The record remains listed while the loop is still live.
