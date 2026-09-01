<!--
name: 'Data: Sandbox install partial result'
description: >-
  Partial-completion message for /sandbox install describing which of the
  sandbox user, credential and network filters landed; emitted as
  <local-command-stdout> command output the model sees.
ccVersion: 2.1.257
variables:
  - DATA_SANDBOX_INSTALL_PARTIAL_STATUS_VAR_0
-->
Install completed (sandbox user: ${{user_not_provisioned:"not provisioned",cred_not_readable:"provisioned, credential not readable",wfp_not_installed:"provisioned"}[n]}, filters: ${DATA_SANDBOX_INSTALL_PARTIAL_STATUS_VAR_0.wfp.state}). Run /sandbox install again to retry.
