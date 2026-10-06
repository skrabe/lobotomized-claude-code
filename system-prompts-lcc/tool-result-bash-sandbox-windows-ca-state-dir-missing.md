<!--
name: 'Tool Result: Bash sandbox Windows CA state dir missing'
description: >-
  Windows sandbox init error when the sandbox-runtime state directory is missing
  and windows-install must run first; surfaces via the required-sandbox init
  failure in the Bash tool result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_0
-->
ensurePersistentWindowsCa: state directory ${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_STATE_DIR_MISSING_VAR_0} does not exist. Run \`npx sandbox-runtime windows-install\` first.
