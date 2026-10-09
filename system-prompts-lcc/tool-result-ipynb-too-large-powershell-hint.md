<!--
name: 'Notebook too large: PowerShell hint'
description: PowerShell commands to read portions of an oversized notebook.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_IPYNB_TOO_LARGE_POWERSHELL_HINT_VAR_0
-->
Use ${TOOL_RESULT_IPYNB_TOO_LARGE_POWERSHELL_HINT_VAR_0} to read specific portions:
  Get-Content <notebook_path> | ConvertFrom-Json | Select-Object -ExpandProperty cells | Select-Object -Skip 100 -First 20 # Cells 100-120
  (Get-Content <notebook_path> | ConvertFrom-Json).cells.Count # Count total cells
  Get-Content <notebook_path> | ConvertFrom-Json | Select-Object -ExpandProperty cells | Where-Object cell_type -eq code | Select-Object -ExpandProperty source
