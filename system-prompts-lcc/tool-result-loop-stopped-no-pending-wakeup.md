<!--
name: 'Tool Result: Loop Stopped (no pending wakeup)'
description: >-
  Model-facing tool_result for stop:true when no dynamic wakeup was pending: the
  dynamic loop ended, but a fixed-interval /loop cron is NOT stopped and must be
  cancelled explicitly. New envelope in 2.1.206.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_LOOP_STOPPED_CRON_DELETE_TOOL
  - TOOL_RESULT_LOOP_STOPPED_REARM_SUFFIX
-->
Loop stopped — any dynamic loop in this session is ended; there was no pending wakeup to cancel. If you are running a fixed-interval /loop (a recurring cron), it is NOT stopped by this call — cancel it with ${TOOL_RESULT_LOOP_STOPPED_CRON_DELETE_TOOL}. ${TOOL_RESULT_LOOP_STOPPED_REARM_SUFFIX}
