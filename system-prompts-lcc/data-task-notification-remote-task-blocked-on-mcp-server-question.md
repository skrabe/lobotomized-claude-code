<!--
name: 'Data: task notification remote task blocked on MCP server question'
description: >-
  Remote-task blocked reason when the cloud session shows an MCP server question
  that cannot be answered locally. It says where to answer it and that the task
  stopped waiting.
ccVersion: 2.1.281
variables:
  - DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_MCP_SERVER_QUESTION_VAR_0
  - DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_MCP_SERVER_QUESTION_VAR_1
-->
the cloud session has shown ${DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_MCP_SERVER_QUESTION_VAR_0}; such a question can't be answered from here. Answer it at ${DATA_TASK_NOTIFICATION_REMOTE_TASK_BLOCKED_ON_MCP_SERVER_QUESTION_VAR_1} and the cloud session will carry on there, but this task has stopped waiting for it.
