<!--
name: Task Notification Container Restarted Work Lost
description: >-
  Task-notification summary telling the model background work was lost when the
  container restarted.
ccVersion: 2.1.247
variables:
  - DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_0
-->
The container running this session was restarted before background work reported back: ${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_0}. That work is lost — no result or further notification will arrive for it. Re-create it if still needed (a long-running server or watcher that nothing is waiting on does not need restarting now), or tell the user what was lost.
