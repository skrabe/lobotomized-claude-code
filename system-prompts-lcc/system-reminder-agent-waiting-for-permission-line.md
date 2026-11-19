<!--
name: 'System Reminder: Agent waiting for permission line'
description: Lists an agent (and its parent) that is waiting for permission to use a tool
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_0
  - SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_1
  - SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_2
-->
Agent ${SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_0}${SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_1.parentAgentId===void 0?"":` (started by agent ${SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_1.parentAgentId})`} is waiting for permission to use ${SYSTEM_REMINDER_AGENT_WAITING_FOR_PERMISSION_LINE_VAR_2}.
