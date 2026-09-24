<!--
name: 'System Reminder: Container restarted, finished tasks undelivered'
description: >-
  Container-restart reminder paragraph listing background tasks that finished
  before the restart but whose results were never delivered to the model.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_FINISHED_TASKS_UNDELIVERED_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_FINISHED_TASKS_UNDELIVERED_VAR_1
-->
These background tasks finished before the restart, but their results were not delivered to you:
${SYSTEM_REMINDER_CONTAINER_RESTARTED_FINISHED_TASKS_UNDELIVERED_VAR_0.join(`
`)}
${SYSTEM_REMINDER_CONTAINER_RESTARTED_FINISHED_TASKS_UNDELIVERED_VAR_1}
