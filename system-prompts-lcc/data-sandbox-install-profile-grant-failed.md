<!--
name: 'Sandbox install: profile grant failed'
description: 'Installed, but the profile could not be made readable; run install again.'
ccVersion: 2.1.325
variables:
  - DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_0
  - DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_1
  - DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_2
  - DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_3
  - DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_4
-->
The sandbox account and network filters are installed, but the tool directories of your user profile could not be made readable to sandboxed commands: the grant ${DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_0?"did not finish in time":"failed"}. Sandboxed commands will not start until that step completes. Run /sandbox install again to retry.${DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_1?` (Details: ${DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_1})`:""}${DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_2(DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_3,DATA_SANDBOX_INSTALL_PROFILE_GRANT_FAILED_VAR_4)}
