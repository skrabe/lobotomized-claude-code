<!--
name: 'Slash Command: /web-setup — GitHub CLI too old'
description: >-
  Tells the model `gh` is logged in but too old for `gh auth token` (needs
  2.17.0+) and names update-or-browser recovery before /web-setup can succeed.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_WEB_SETUP_GH_CLI_TOO_OLD_VAR_0
-->
GitHub CLI is logged in, but this version is too old to share its login (\`gh auth token\` needs GitHub CLI 2.17.0 or newer). Update it via https://cli.github.com/, or connect GitHub on the web: ${SLASH_COMMAND_WEB_SETUP_GH_CLI_TOO_OLD_VAR_0}
