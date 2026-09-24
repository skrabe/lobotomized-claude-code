<!--
name: 'System Reminder: Container restarted, stopped-tasks list'
description: >-
  Stopped-background-tasks paragraph pushed into the container-restarted
  reminder, listing the tasks and asking to re-create them if still needed.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_0
-->
The following background tasks were running and are now stopped:
${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_0.join(`
`)}
Re-create them if still needed.
