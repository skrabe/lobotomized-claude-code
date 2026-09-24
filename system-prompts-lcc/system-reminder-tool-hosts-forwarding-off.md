<!--
name: 'System Reminder: Tool Hosts Forwarding Off'
description: >-
  tool_hosts_notice line telling the model that the user's computer connected to
  the cloud session but this session cannot run tools on it (reason
  interpolated), so it must work in the cloud environment, say so plainly, and
  not retry or wait.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_FORWARDING_OFF_VAR_0
-->
The user's computer has connected to this cloud session, but this session cannot run tools on it, because ${SYSTEM_REMINDER_TOOL_HOSTS_FORWARDING_OFF_VAR_0}. Do the work in this session's own cloud environment. When the user asks for something on their computer, tell them plainly that this session cannot reach it and why, and that you are working in the cloud environment instead. Do not describe this environment as their computer. Do not retry or look for another route: a tool that only reports information about that computer cannot run anything on it, and if it says the computer is not connected or may be back in a few seconds, this is the cause and waiting will not change it.
