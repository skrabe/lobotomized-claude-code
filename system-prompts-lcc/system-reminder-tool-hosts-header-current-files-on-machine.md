<!--
name: 'Tool Hosts Notice: Header Current Files On Machine'
description: >-
  Off-sync header: the user's current project files live on the named host, the
  machine argument runs the call there, and only scratch work belongs here.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_2
-->
Machines attached to this session — ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_0.livesThere}: ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_1} to run it on that machine, and ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_0.work}; omit it (runs here, ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_CURRENT_FILES_ON_MACHINE_VAR_2()}) only for work that does not need the user's current files — scratch computation, fetching docs, tools you install for yourself:
