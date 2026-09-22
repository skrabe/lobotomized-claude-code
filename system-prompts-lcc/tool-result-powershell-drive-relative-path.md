<!--
name: 'Tool Result: PowerShell drive-relative path'
description: >-
  Permission-denial reason returned to the model when a PowerShell path is
  drive-relative and cannot be statically validated; copied into the tool_result
  message.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_0
  - TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_1
  - TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_2
-->
Path '${TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_0?TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_1:TOOL_RESULT_POWERSHELL_DRIVE_RELATIVE_PATH_VAR_2}' is drive-relative (resolves against the per-drive current directory, which cannot be statically validated) and requires manual approval
