<!--
name: 'Task Notification: Agent Turn-Limit Partial Result'
description: >-
  Status clause in the agent task-notification summary when the agent stopped at
  its max-turn limit, telling the parent to continue via the task-id.
ccVersion: 2.1.246
variables:
  - DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_0
  - DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_1
-->
stopped at its ${DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_0}-turn limit (partial result; ${DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_1} to task-id to continue)
