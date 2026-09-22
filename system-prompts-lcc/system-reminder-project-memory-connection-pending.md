<!--
name: 'System Reminder: Project Memory Connection Pending'
description: >-
  Tells the model that a newly selected shared project-memory connection is
  still being established and to re-check the memory tools before relying on it.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_PENDING_VAR_0
  - SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_PENDING_VAR_1
-->
The user picked a project's shared memory in /memory and the connection is still being set up; nothing is connected yet. Before relying on the ${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_PENDING_VAR_0} tools, call ${SYSTEM_REMINDER_PROJECT_MEMORY_CONNECTION_PENDING_VAR_1} with no arguments: once it lists connected stores, read your teammates' shared memories and save new shared learnings through those tools as their prompts describe.
