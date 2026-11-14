<!--
name: 'Tool Result: Bash sandbox Windows CA state dir missing'
description: >-
  Windows sandbox init error when the sandbox-runtime state directory is missing
  and windows-install must run first; surfaces via the required-sandbox init
  failure in the Bash tool result.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_1
-->
ensurePersistentWindowsCa: state directory ${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_0} does not exist. Run \`${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_1}\` first.
