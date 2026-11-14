<!--
name: 'Data: Sandbox install stale allow paths'
description: >-
  Warns that paths set-up no longer means to open may still be readable through
  entries it could not remove
ccVersion: 2.1.325
variables:
  - DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_0
  - DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_1
  - DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_2
  - DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_3
-->
Credential stores are denied, but ${DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_0.length} path(s) that set-up no longer means to open may still be read through an entry it could not remove: ${DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_0.slice(0,10).map((DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_1)=>`${DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_2(DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_1.path)} (${DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_3(DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_1.reason)})`).join("; ")}${DATA_SANDBOX_INSTALL_STALE_ALLOW_PATHS_VAR_0.length>10?"; …":""}; a session start tries local paths again.
