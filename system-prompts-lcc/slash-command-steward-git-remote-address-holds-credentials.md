<!--
name: 'Slash command: Steward git remote address holds credentials'
description: Refuses a remote whose address embeds a password or token
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_HOLDS_CREDENTIALS_VAR_0
-->
${SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_HOLDS_CREDENTIALS_VAR_0.name}'s address holds a password, or a user's name that is long enough to be a token: keep it in a git credential helper, and take it out of the address with git remote set-url
