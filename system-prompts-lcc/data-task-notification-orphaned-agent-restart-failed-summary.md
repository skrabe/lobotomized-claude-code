<!--
name: 'Data: Task notification orphaned agent restart failed summary'
description: >-
  Task-notification summary that a background agent from the previous session
  (or one stopped by a container restart) could not be restarted, with the
  reason
ccVersion: 2.1.328
variables:
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_0
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_1
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_2
-->
Background agent "${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_0(DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_1.description)}" ${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_1.stopUntold?"was stopped by a restart of the container and":"from the previous session"} couldn't be restarted: ${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_0(DATA_TASK_NOTIFICATION_ORPHANED_AGENT_RESTART_FAILED_SUMMARY_VAR_2)}
