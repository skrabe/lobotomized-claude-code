<!--
name: 'Tool result: PowerShell Windows sandbox exclusion no prompt'
description: >-
  Blocks a Windows PowerShell command whose sandbox exclusion cannot apply
  because no permission prompt is available
ccVersion: 2.1.234
-->
Enterprise policy requires sandboxing, but the sandbox is unavailable on Windows. The command matches a sandbox exclusion pattern, but exclusions only exempt a command where a permission prompt can approve the unsandboxed run, and none is available here. Shell command execution is blocked by policy.
