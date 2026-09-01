<!--
name: Compound cd invalidates relative paths
description: >-
  PowerShell command-safety reason surfaced to the model when a compound command
  changes cwd so relative paths cannot be validated.
ccVersion: 2.1.206
-->
Compound command changes working directory (Set-Location/Push-Location/Pop-Location/New-PSDrive) — relative paths cannot be validated against the original cwd and require manual approval
