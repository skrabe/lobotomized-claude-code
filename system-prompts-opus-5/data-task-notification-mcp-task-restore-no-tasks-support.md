<!--
name: 'MCP Task Restore: Modern Protocol Lacks Tasks Support'
description: >-
  Failure detail from _Sf during MCP task restore, wrapped by M8a as a <result>
  task-notification injected into the model context.
ccVersion: 2.1.238
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_1
  - DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_2
-->
server '${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_0}' ${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_1} on ${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_2?`protocol revision ${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_2}`:"a modern-era protocol revision"}, which has no tasks support
