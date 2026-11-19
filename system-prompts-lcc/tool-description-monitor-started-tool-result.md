<!--
name: 'Tool Result: Monitor Started'
description: >-
  Monitor tool result telling the model the monitor started and it will be
  notified on events; keep working, do not poll.
ccVersion: 2.1.328
variables:
  - TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0
  - TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_1
  - TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_2
  - TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_3
-->
Monitor started (task ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0.taskId}, ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_1}). You will be notified on each event. Keep working — do not poll or sleep. ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_2()?"An event that arrives after your reply is not the user's reply.":"Events may arrive while you are waiting for the user — an event is not their reply."}${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_0.keptInSandboxByCheck===!0?` ${TOOL_DESCRIPTION_MONITOR_STARTED_TOOL_RESULT_VAR_3}`:""}
