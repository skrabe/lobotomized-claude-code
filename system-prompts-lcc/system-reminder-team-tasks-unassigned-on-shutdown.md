<!--
name: 'System Reminder: Team Tasks Unassigned On Shutdown'
description: >-
  Team-coordination inbox message that a teammate shut down leaving tasks
  unassigned; prompts reassignment via TaskUpdate.
ccVersion: 2.1.178
variables:
  - SYSTEM_REMINDER_TEAM_TASKS_UNASSIGNED_ON_SHUTDOWN_VAR_0
  - SYSTEM_REMINDER_TEAM_TASKS_UNASSIGNED_ON_SHUTDOWN_VAR_1
-->
 ${SYSTEM_REMINDER_TEAM_TASKS_UNASSIGNED_ON_SHUTDOWN_VAR_0.length} task(s) were unassigned: ${SYSTEM_REMINDER_TEAM_TASKS_UNASSIGNED_ON_SHUTDOWN_VAR_1}. Use TaskList to check availability and TaskUpdate with owner to reassign them to idle teammates.
