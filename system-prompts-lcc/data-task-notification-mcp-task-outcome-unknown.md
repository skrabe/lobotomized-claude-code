<!--
name: 'Data: Task notification MCP task outcome unknown'
description: >-
  Notification body saying an MCP task's outcome is unknown and how to proceed
  safely
ccVersion: 2.1.318
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_OUTCOME_UNKNOWN_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_OUTCOME_UNKNOWN_VAR_1
-->
Task outcome unknown: ${DATA_TASK_NOTIFICATION_MCP_TASK_OUTCOME_UNKNOWN_VAR_0[DATA_TASK_NOTIFICATION_MCP_TASK_OUTCOME_UNKNOWN_VAR_1]}.
Claude Code has stopped following this task, so no result will arrive. It may have completed, failed, stopped part-way or still be running: tell the user its outcome is unknown, not that it is done or failed.
