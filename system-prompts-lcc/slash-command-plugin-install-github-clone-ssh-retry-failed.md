<!--
name: 'Plugin install: GitHub clone failed over HTTPS and SSH'
description: >-
  Install failure after both HTTPS and SSH clones of a GitHub plugin source
  fail, with remediation guidance.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_2
-->
${SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_1)}
The retry over SSH failed too: ${SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_GITHUB_CLONE_SSH_RETRY_FAILED_VAR_2)}
Check the repository and ref in the marketplace entry and that github.com can be reached. If the repository is private, add an SSH key to your GitHub account or set up a git credential helper for https://github.com. Then install again.
