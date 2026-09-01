<!--
name: 'System Reminder: Container restarted, tasks stopped'
description: >-
  Reminder listing background tasks stopped by a container restart, prompting
  re-creation.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_1
-->
<system-reminder>
The container was restarted. The following background tasks were running and are now stopped:
${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_0.map((SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_1)=>`- ${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_2(SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_1.description||"(no description)")} (task ${SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_2(SYSTEM_REMINDER_CONTAINER_RESTARTED_TASKS_STOPPED_VAR_1.task_id)})`).join(`
`)}
Re-create them if still needed.
</system-reminder>
