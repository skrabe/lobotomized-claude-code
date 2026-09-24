<!--
name: 'System Reminder: Container restarted, tasks stopped'
description: >-
  Meta reminder after a container restart. It wraps the lists of background
  tasks that were stopped and of tasks that finished but whose results were not
  delivered.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_0
-->
<system-reminder>
The container was restarted. ${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_0.join(`
`)}
</system-reminder>
