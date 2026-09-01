<!--
name: 'Tool Result: Monitor Started'
description: >-
  Monitor/Task tool result telling the model the monitor started and it will be
  notified on events; keep working, do not poll.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0
-->
Monitor started (task ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0.taskId}, ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0.persistent?"persistent — runs until TaskStop or session end":`timeout ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0.timeoutMs}ms`}). You will be notified on each event. Keep working — do not poll or sleep. Events may arrive while you are waiting for the user — an event is not their reply.
