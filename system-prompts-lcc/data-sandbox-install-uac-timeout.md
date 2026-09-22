<!--
name: 'Data: Sandbox Install UAC Timeout'
description: >-
  Status message from /sandbox install on Windows when the elevation prompt
  times out after two minutes.
ccVersion: 2.1.221
variables:
  - DATA_SANDBOX_INSTALL_UAC_TIMEOUT_VAR_0
-->

The install timed out after 2 minutes: ${DATA_SANDBOX_INSTALL_UAC_TIMEOUT_VAR_0}. If an elevation prompt was showing, run /sandbox install again and respond to the prompt. If no prompt appeared, the installer may be blocked on this machine — run /sandbox to check sandbox status.
