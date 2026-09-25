<!--
name: 'Slash Command: /install-github-app — cancelled after partial setup'
description: >-
  Tells the model the GitHub App installation was cancelled by the user partway
  through and lists the steps already completed in the selected repository, so
  it does not assume setup is either absent or complete.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_INSTALL_GITHUB_APP_CANCELLED_PARTIAL_SETUP_VAR_0
  - SLASH_COMMAND_INSTALL_GITHUB_APP_CANCELLED_PARTIAL_SETUP_VAR_1
-->
Installation cancelled by user. Already done in ${SLASH_COMMAND_INSTALL_GITHUB_APP_CANCELLED_PARTIAL_SETUP_VAR_0.selectedRepoName}: ${SLASH_COMMAND_INSTALL_GITHUB_APP_CANCELLED_PARTIAL_SETUP_VAR_1.alreadyDone.join(", ")}.
