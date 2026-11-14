<!--
name: 'Tool Result: Bash sandbox Windows CA user not provisioned'
description: >-
  Sandbox init failure reason when ensurePersistentWindowsCa runs with an
  unprovisioned sandbox user; surfaces in the 'Sandbox is required but failed to
  initialize' Bash error
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_USER_NOT_PROVISIONED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_USER_NOT_PROVISIONED_VAR_1
-->
ensurePersistentWindowsCa: sandbox user is not provisioned (user=${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_USER_NOT_PROVISIONED_VAR_0.provisioned}, cred=${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_USER_NOT_PROVISIONED_VAR_0.credPresent}). Run \`${TOOL_RESULT_BASH_SANDBOX_WINDOWS_CA_USER_NOT_PROVISIONED_VAR_1}\` first.
