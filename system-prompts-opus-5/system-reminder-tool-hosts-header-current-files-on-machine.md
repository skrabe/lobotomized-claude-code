<!--
name: 'Tool Hosts Notice: Header Current Files On Machine'
description: >-
  Off-sync header: the user's current project files live on the named host; only
  scratch work that needs none of them should run here.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_3
-->
Machines attached to this session — the user's CURRENT project files live on ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_0}, not here: ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_1} to run it on that machine, and ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_2}; omit it (runs here, ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_3()}) only for work that does not need the user's current files — scratch computation, fetching docs, tools you install for yourself:
