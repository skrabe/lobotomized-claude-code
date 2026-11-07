<!--
name: 'Tool Result: Bash sandbox init failed, own command not run'
description: >-
  Error when the sandbox fails to initialize for a Claude Code internal command:
  the command was not run, the sandbox stays on and retries on the next command
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_BASH_SANDBOX_ENABLED_INIT_FAILED_OWN_COMMAND_NOT_RUN_VAR_0
-->
Sandbox is enabled but failed to initialize${TOOL_RESULT_BASH_SANDBOX_ENABLED_INIT_FAILED_OWN_COMMAND_NOT_RUN_VAR_0}. This command of Claude Code's own was not run; the sandbox stays on, and the next command tries to start it again.
