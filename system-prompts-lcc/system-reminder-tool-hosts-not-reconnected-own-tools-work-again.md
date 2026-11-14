<!--
name: 'System Reminder: Tool hosts not reconnected own tools work again'
description: >-
  Tells the model the machines' own mcp tools work again once they have
  reconnected
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_OWN_TOOLS_WORK_AGAIN_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_OWN_TOOLS_WORK_AGAIN_VAR_1
-->
${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_OWN_TOOLS_WORK_AGAIN_VAR_0?"That machine's":"Those machines'"} own tools (mcp__${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_OWN_TOOLS_WORK_AGAIN_VAR_1}__…) work again once ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_OWN_TOOLS_WORK_AGAIN_VAR_0?"it has":"they have"} reconnected.
