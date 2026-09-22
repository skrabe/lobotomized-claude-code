<!--
name: 'System Reminder: Project Memory Connection Changed'
description: >-
  Introduces the system reminder sent to the model after the session's
  project-memory connection changes.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_0
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_1
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_2
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_3
-->
The project memory connected to this session has changed: ${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_0?`the project the user picked in /memory is no longer available, so ${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_1(SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_2.project)} is connected instead`:SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_2.project.kind==="default"?"the user picked a project in /memory, and the default project memory is what is now connected":`the user picked ${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_1(SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_2.project)} in /memory`}.${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_CHANGED_VAR_3}
