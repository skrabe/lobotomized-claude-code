<!--
name: 'Data: Task notification container restarted work lost'
description: >-
  Task notification after a container restart listing background work that never
  reported back, with a slot for the lost/resumable clause, asking to re-create
  it if needed or tell the user what was lost
ccVersion: 2.1.292
variables:
  - DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_0
  - DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_1
-->
The container running this session was restarted before background work reported back: ${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_0}. ${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_WORK_LOST_VAR_1} if still needed (a long-running server or watcher that nothing is waiting on does not need restarting now), or tell the user what was lost.
