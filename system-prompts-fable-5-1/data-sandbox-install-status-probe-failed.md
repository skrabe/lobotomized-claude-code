<!--
name: 'Data: Sandbox install status probe failed'
description: >-
  Error message for /sandbox install when the post-install status probe could
  not be read back; emitted as <local-command-stdout> command output the model
  sees.
ccVersion: 2.1.214
variables:
  - DATA_SANDBOX_INSTALL_STATUS_PROBE_FAILED_VAR_0
-->
The installer ran, but the sandbox status couldn't be read back afterwards: ${DATA_SANDBOX_INSTALL_STATUS_PROBE_FAILED_VAR_0}. Run /sandbox to check the current status.
