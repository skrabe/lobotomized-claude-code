<!--
name: 'Data: task notification container restarted timers lost'
description: >-
  Task notification after a container restart that pending timers will not fire
  and should be rescheduled.
ccVersion: 2.1.291
variables:
  - DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_TIMERS_LOST_VAR_0
  - DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_TIMERS_LOST_VAR_1
-->
${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_TIMERS_LOST_VAR_0.length>0?"Timers that were pending in that container will not fire either":"The container running this session was restarted, so these pending timers will not fire"}: ${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_TIMERS_LOST_VAR_1}. Schedule each again if still needed (do the work of an overdue one now)${DATA_TASK_NOTIFICATION_CONTAINER_RESTARTED_TIMERS_LOST_VAR_0.length>0?"":", or tell the user what was lost"}.
