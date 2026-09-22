<!--
name: 'Tool Result: Notebook outputs too large — PowerShell recovery command'
description: >-
  The Get-Content/ConvertFrom-Json equivalent offered on Windows for reading an
  individual notebook cell whose outputs were too large to return.
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POWERSHELL_RECOVERY_VAR_0
  - TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POWERSHELL_RECOVERY_VAR_1
-->
${TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POWERSHELL_RECOVERY_VAR_0} with: Get-Content <notebook_path> | ConvertFrom-Json | Select-Object -ExpandProperty cells | Select-Object -Index ${TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POWERSHELL_RECOVERY_VAR_1} | Select-Object -ExpandProperty outputs
