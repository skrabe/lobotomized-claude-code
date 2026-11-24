<!--
name: MCP task ending redelivered
description: 'Saved MCP task notification redelivered on resume, with ignore-if-seen note.'
ccVersion: 2.1.331
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_ENDING_REDELIVERED_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_ENDING_REDELIVERED_VAR_1
-->
This notification was written at ${new DATA_TASK_NOTIFICATION_MCP_TASK_ENDING_REDELIVERED_VAR_0(DATA_TASK_NOTIFICATION_MCP_TASK_ENDING_REDELIVERED_VAR_1).toISOString()}. It is delivered now because this session was resumed and its conversation does not contain it. If you have already seen it, ignore this copy.
