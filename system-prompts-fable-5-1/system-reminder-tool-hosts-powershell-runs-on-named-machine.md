<!--
name: 'Tool Hosts Notice: PowerShell Runs On Named Machine'
description: >-
  PowerShell routing fragment, when more than one PowerShell host is attached,
  saying the call runs on the machine the machine argument names.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_2
-->
runs on the machine "${SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_0}" names (${SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_1(SYSTEM_REMINDER_TOOL_HOSTS_POWERSHELL_RUNS_ON_NAMED_MACHINE_VAR_2)} — it must name one)
