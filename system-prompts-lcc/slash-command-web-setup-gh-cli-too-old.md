<!--
name: 'Slash Command: /web-setup — GitHub CLI too old'
description: >-
  Returned when gh is signed in but older than 2.17.0 so gh auth token is
  unavailable; points to an update or the web onboarding link.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_WEB_SETUP_GH_CLI_TOO_OLD_VAR_0
-->
GitHub CLI is signed in, but this version is too old to share its sign-in (\`gh auth token\` needs GitHub CLI 2.17.0 or newer). Update it via https://cli.github.com/, or connect GitHub on the web: ${SLASH_COMMAND_WEB_SETUP_GH_CLI_TOO_OLD_VAR_0}
