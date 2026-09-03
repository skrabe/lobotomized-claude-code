<!--
name: 'Slash Command: /install-github-app — install failed with an error'
description: >-
  Gives the model the specific installation error plus the manual-setup doc URL,
  which is the recovery step it should hand the user.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_INSTALL_GITHUB_APP_INSTALL_ERROR_VAR_0
  - SLASH_COMMAND_INSTALL_GITHUB_APP_INSTALL_ERROR_VAR_1
-->
Couldn't install GitHub App: ${SLASH_COMMAND_INSTALL_GITHUB_APP_INSTALL_ERROR_VAR_0.error}
For manual setup instructions, see: ${SLASH_COMMAND_INSTALL_GITHUB_APP_INSTALL_ERROR_VAR_1}
