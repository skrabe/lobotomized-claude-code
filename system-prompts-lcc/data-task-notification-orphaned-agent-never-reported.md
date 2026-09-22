<!--
name: 'Task Notification: Orphaned Agent Result Never Reported'
description: >-
  Task-notification summary injected on resume when a background agent finished
  in the previous session but its result was never reported.
ccVersion: 2.1.265
variables:
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_NEVER_REPORTED_VAR_0
  - DATA_TASK_NOTIFICATION_ORPHANED_AGENT_NEVER_REPORTED_VAR_1
-->
Background agent "${DATA_TASK_NOTIFICATION_ORPHANED_AGENT_NEVER_REPORTED_VAR_0(DATA_TASK_NOTIFICATION_ORPHANED_AGENT_NEVER_REPORTED_VAR_1.description)}" finished before the previous session ended, but its result was never reported
