<!--
name: 'Slash Command: /privacy-settings signed-in account note'
description: >-
  /privacy-settings output line naming the account Claude Code is signed in as
  and asking to switch on claude.ai if it differs.
ccVersion: 2.1.322
variables:
  - SLASH_COMMAND_PRIVACY_SETTINGS_SIGNED_IN_ACCOUNT_VAR_0
-->
Claude Code is signed in as ${SLASH_COMMAND_PRIVACY_SETTINGS_SIGNED_IN_ACCOUNT_VAR_0}. If claude.ai shows a different account, switch to ${SLASH_COMMAND_PRIVACY_SETTINGS_SIGNED_IN_ACCOUNT_VAR_0} before changing anything.
