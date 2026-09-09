<!--
name: 'Slash Command: /design Subcommand Not Offered'
description: >-
  /design getPromptForCommand early-return telling the model that a dedicated
  subcommand (consent/revoke/sync/login) is for the user to type themselves and
  this session does not offer it.
ccVersion: 2.1.265
variables:
  - SLASH_COMMAND_DESIGN_SUBCOMMAND_NOT_OFFERED_VAR_0
-->
\`/design ${SLASH_COMMAND_DESIGN_SUBCOMMAND_NOT_OFFERED_VAR_0}\` is for the user to type themselves, in an interactive Claude Code terminal signed in to claude.ai; if they already did, this session does not offer it (organization policy or sign-in). Say so in one line and stop.
