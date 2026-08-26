<!--
name: 'Slash Command: /web-setup — GitHub CLI check failed'
description: >-
  Tells the model /web-setup could not check `gh` login status and names `gh
  auth status` or the browser onboarding URL as recovery.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_WEB_SETUP_GH_CLI_CHECK_FAILED_VAR_0
  - SLASH_COMMAND_WEB_SETUP_GH_CLI_CHECK_FAILED_VAR_1
-->
Couldn't check GitHub CLI login status${SLASH_COMMAND_WEB_SETUP_GH_CLI_CHECK_FAILED_VAR_0}. Run \`gh auth status\` to check, or connect GitHub on the web: ${SLASH_COMMAND_WEB_SETUP_GH_CLI_CHECK_FAILED_VAR_1()}/onboarding?step=alt-auth
