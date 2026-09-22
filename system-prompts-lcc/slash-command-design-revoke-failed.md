<!--
name: 'Slash Command: Design revoke failed'
description: 'Type:text result of /design revoke when revoking Design agent access throws.'
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_DESIGN_REVOKE_FAILED_VAR_0
  - SLASH_COMMAND_DESIGN_REVOKE_FAILED_VAR_1
-->
Couldn't revoke Design agent access for ${"your Claude Design projects"} — ${SLASH_COMMAND_DESIGN_REVOKE_FAILED_VAR_0(SLASH_COMMAND_DESIGN_REVOKE_FAILED_VAR_1)}. Try again, or run /design-login to authorize Claude Design for this account.
