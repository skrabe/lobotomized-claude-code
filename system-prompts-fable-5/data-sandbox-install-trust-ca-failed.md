<!--
name: 'Data: Sandbox Install CA Trust Failed'
description: >-
  Partial-status message from /sandbox install when the sandbox TLS inspection
  CA could not be trusted for the sandbox user.
ccVersion: 2.1.221
variables:
  - DATA_SANDBOX_INSTALL_TRUST_CA_FAILED_VAR_0
-->

The sandbox TLS inspection CA couldn't be trusted for the sandbox user: ${DATA_SANDBOX_INSTALL_TRUST_CA_FAILED_VAR_0}. Sandboxed HTTPS won't work — run /sandbox install again to retry.
