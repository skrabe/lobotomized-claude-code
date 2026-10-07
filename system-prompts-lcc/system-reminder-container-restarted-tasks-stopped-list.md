<!--
name: 'System Reminder: Container restarted tasks stopped list'
description: >-
  Lists background tasks that were running and are now stopped after a container
  restart, asking to re-create them if still needed
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_1
-->
The following background tasks were running and are now stopped:
${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_0.join(`
`)}
${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_1?`${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_LIST_VAR_1} Re-create anything else`:"Re-create them"} if still needed.
