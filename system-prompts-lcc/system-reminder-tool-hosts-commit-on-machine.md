<!--
name: 'System Reminder: Tool Hosts Commit On Machine'
description: >-
  Clause in the tool hosts notice's Git line: the project's real copy is on the
  attached machine, so make any commit or push the user asks for there if that
  folder is a git checkout.
ccVersion: 2.1.317
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_COMMIT_ON_MACHINE_VAR_0
-->
 The project's real copy is on ${SYSTEM_REMINDER_TOOL_HOSTS_COMMIT_ON_MACHINE_VAR_0}: when the user asks for a commit or a push, make it there, if that folder is a git checkout.
