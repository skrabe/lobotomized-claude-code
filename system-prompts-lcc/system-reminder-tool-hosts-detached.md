<!--
name: 'System Reminder: Tool hosts detached'
description: >-
  Tells the model the machine is no longer attached, where to run commands, and
  to say so if the task needs that machine
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_DETACHED_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_DETACHED_VAR_1
-->
${SYSTEM_REMINDER_TOOL_HOSTS_DETACHED_VAR_0}; ${SYSTEM_REMINDER_TOOL_HOSTS_DETACHED_VAR_1()}. If the task needs that machine's files, tools or logins, say so instead of doing it here.
