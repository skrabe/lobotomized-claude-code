<!--
name: 'Slash command: Steward git remote address unreadable'
description: Reports a remote address /steward can't read or a split fetch/push address
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_1
  - SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_2
-->
${SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_0===void 0?SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_1:SLASH_COMMAND_STEWARD_GIT_REMOTE_ADDRESS_UNREADABLE_VAR_2} has an address that /steward can't read (it reads https://HOST/PATH, ssh://HOST/PATH and HOST:PATH), or fetches from one address and pushes to another: see git remote -v
