<!--
name: 'Task Notification: Background Agents Aggregate Lost'
description: >-
  Aggregate task-notification body stating several background agents were
  running at exit and lost their in-process state.
ccVersion: 2.1.268
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_AGGREGATE_LOST_VAR_0
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_AGGREGATE_LOST_VAR_1
-->
They were running when the previous Claude Code process exited and did not complete. Their in-process state was lost. ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_AGGREGATE_LOST_VAR_0?"Launch them again if their reports are still needed.":DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_AGGREGATE_LOST_VAR_1?"Do not assume the tasks landed; launch them again if their results are still needed.":"Check each agent's worktree/output for partial work before assuming the tasks landed."}
