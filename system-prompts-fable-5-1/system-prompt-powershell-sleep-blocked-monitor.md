<!--
name: 'System Prompt: PowerShell sleep blocked (use Monitor)'
description: >-
  PowerShell validateInput tool_result blocking a sleep, telling the model to
  use Monitor with an until-loop or run_in_background
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_POWERSHELL_SLEEP_BLOCKED_MONITOR_VAR_0
-->
Blocked: ${SYSTEM_PROMPT_POWERSHELL_SLEEP_BLOCKED_MONITOR_VAR_0}. To wait for a condition, use Monitor with an until-loop (e.g. \`until <check>; do sleep 2; done\`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
