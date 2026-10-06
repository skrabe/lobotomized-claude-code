<!--
name: 'Tool result: hook PowerShell executable not found'
description: >-
  Hook execution error (embedded in a WorktreeCreate hook failure) when a hook
  sets shell: powershell but no pwsh/powershell is on PATH
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_HOOK_POWERSHELL_NOT_FOUND_VAR_0
-->
Hook "${TOOL_RESULT_HOOK_POWERSHELL_NOT_FOUND_VAR_0.command}" has shell: 'powershell' but no PowerShell executable (pwsh or powershell) was found on PATH. Install PowerShell, or remove "shell": "powershell" to use bash.
