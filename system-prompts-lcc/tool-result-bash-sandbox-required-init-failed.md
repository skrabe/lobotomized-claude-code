<!--
name: 'Tool Result: Bash sandbox required but init failed'
description: >-
  Bash/PowerShell tool error when the sandbox is required but failed to
  initialize, with retry advice
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SANDBOX_REQUIRED_INIT_FAILED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_REQUIRED_INIT_FAILED_VAR_1
-->
Sandbox is required but failed to initialize${TOOL_RESULT_BASH_SANDBOX_REQUIRED_INIT_FAILED_VAR_0}. ${TOOL_RESULT_BASH_SANDBOX_REQUIRED_INIT_FAILED_VAR_1().configBuildFailed?"Fix the sandbox settings to retry (a --settings file is pinned for the process: restart).":"Restart to retry."}
