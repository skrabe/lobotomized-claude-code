<!--
name: 'Tool Hosts Notice: Header Separate Copy'
description: >-
  Separate-copy header: this checkout is primary, the folder on the host is the
  user's unsynced copy, and the machine argument runs a call on that copy only.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_2
-->
Machines attached to this session — ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_0.twoCopies}: ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_1} to run it on that machine, where it acts on that copy only; omit it to run here (${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_SEPARATE_COPY_VAR_2()}, the default):
