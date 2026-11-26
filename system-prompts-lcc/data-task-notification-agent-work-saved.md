<!--
name: 'Task Notification: Agent work so far saved'
description: Task-notification note that a rate-limited agent's work so far is saved.
ccVersion: 2.1.332
variables:
  - DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_0
  - DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_1
  - DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_2
-->
 This agent's work so far is saved.${DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_0?` The limit ${DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_0}.`:""}${DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_1===!1?"":DATA_TASK_NOTIFICATION_AGENT_WORK_SAVED_VAR_2}
