<!--
name: 'Tool Hosts Correction: Host Restarted Command Lost'
description: >-
  Late correction that Claude Code on the host restarted and the command was
  lost with it, so effects should be checked before repeating it.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_HOST_RESTARTED_COMMAND_LOST_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_HOST_RESTARTED_COMMAND_LOST_VAR_1
-->
${SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_HOST_RESTARTED_COMMAND_LOST_VAR_0} Claude Code on ${SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_HOST_RESTARTED_COMMAND_LOST_VAR_1.hostName} has restarted since, and the command was lost with it — it may have partially run before the restart; check its effects before repeating it.
