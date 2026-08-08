<!--
name: 'MCP Task Restore: Modern Protocol Lacks Tasks Support'
description: >-
  Failure detail assigned to `s` in syy() (MCP task restore-after-resume) and
  threaded into `S3s({…statusMessage:`${a}: ${s}`})`, which E3s() wraps as a
  `<result>` task-notification body injected into the model's context when a
  resumed MCP task cannot be reattached.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_1
-->

server '${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_0.serverName}' reconnected on ${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_1?`protocol revision ${DATA_TASK_NOTIFICATION_MCP_TASK_RESTORE_NO_TASKS_SUPPORT_VAR_1}`:"a modern-era protocol revision"}, which has no tasks support
