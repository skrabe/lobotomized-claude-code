<!--
name: 'Tool Hosts Notice: Host Re-announced By New Client'
description: >-
  tool_hosts_notice bullet when a machine is now served by a different attached
  client than before, with the re-announce UTC time.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_REANNOUNCED_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_REANNOUNCED_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HOST_REANNOUNCED_VAR_0} is now served by a different attached client of this session than before (re-announced at ${SYSTEM_REMINDER_TOOL_HOSTS_HOST_REANNOUNCED_VAR_1} UTC).
