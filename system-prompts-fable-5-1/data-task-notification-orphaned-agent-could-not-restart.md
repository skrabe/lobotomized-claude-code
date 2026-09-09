<!--
name: 'Task Notification: Orphaned Agent Restart Failed'
description: >-
  Task-notification summary injected on resume when a background agent from the
  previous session could not be automatically restarted.
ccVersion: 2.1.265
variables:
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_0
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_1
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_2
-->
Background agent "${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_0(DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_1.description)}" from the previous session couldn't be restarted: ${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_0(DATA_TASK_NOTIFICATION_ORPHANED_AGENT_COULD_NOT_RESTART_VAR_2)}
