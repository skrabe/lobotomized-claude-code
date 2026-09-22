<!--
name: 'System Reminder: Tool Hosts Look For It There'
description: >-
  Fallback how-to when the host serves no file tools: look for a missing file
  there with the host shell and the machine argument.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_2
-->
look for it there with ${SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_0(SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_1).tool} and "${SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_2}" (${SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_0(SYSTEM_REMINDER_TOOL_HOSTS_LOOK_FOR_IT_THERE_VAR_1).look})
