<!--
name: Bash Sandbox Windows Mapped-Drive Error
description: >-
  Replaces the Bash tool's stderr when a sandboxed Windows command exits 16
  because the cwd is a mapped network drive, telling the model to move to a
  local-drive workspace.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_MAPPED_DRIVE_VAR_0
-->

The sandbox can't run commands from a network drive${TOOL_RESULT_BASH_SANDBOX_WINDOWS_MAPPED_DRIVE_VAR_0.drive?` (${TOOL_RESULT_BASH_SANDBOX_WINDOWS_MAPPED_DRIVE_VAR_0.drive})`:""}: mapped drives don't exist for the sandbox account. Use a workspace on a local drive.
