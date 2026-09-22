<!--
name: 'Data: Sandbox Install Ambient Write-Deny Failed'
description: >-
  Inner srt-win install error interpolated into the /sandbox install local-jsx
  onDone message when ambient write-deny stamping of world-writable system dirs
  fails.
ccVersion: 2.1.237
variables:
  - DATA_SANDBOX_INSTALL_AMBIENT_WRITE_DENY_FAILED_VAR_0
-->
srt-win install: ambient write-deny stamping failed (stock world-writable system dirs could not be deny-stamped for the sandbox user): ${DATA_SANDBOX_INSTALL_AMBIENT_WRITE_DENY_FAILED_VAR_0}
