<!--
name: 'Bash tool result: MXC sandbox backend cannot run here'
description: >-
  Explains the MXC sandbox backend cannot run on this host and how
  sandbox.windows.backend can be changed to use the sandbox account backend.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_SANDBOX_MXC_CANNOT_RUN_HERE_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_MXC_CANNOT_RUN_HERE_VAR_1
-->
the MXC sandbox backend cannot run here: ${TOOL_RESULT_BASH_SANDBOX_MXC_CANNOT_RUN_HERE_VAR_0.replace(TOOL_RESULT_BASH_SANDBOX_MXC_CANNOT_RUN_HERE_VAR_1,"").replace(/\.$/,"")}. Whoever manages the sandbox settings can set sandbox.windows.backend to "sandboxuser" and run claude sandbox install to use the sandbox account backend at the next start of Claude Code. Changing sandbox settings is for the user or their administrator to decide
