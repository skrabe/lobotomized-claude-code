<!--
name: 'System Reminder: Tool Hosts Commit On Machine'
description: >-
  Clause in the tool hosts notice's Git line: the real checkout is on the
  attached machine, so make any commit or push the user asks for there.
ccVersion: 2.1.285
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_COMMIT_ON_MACHINE_VAR_0
-->
 The project's real checkout is on ${SYSTEM_REMINDER_TOOL_HOSTS_COMMIT_ON_MACHINE_VAR_0}: when the user asks for a commit or a push, make it there.
