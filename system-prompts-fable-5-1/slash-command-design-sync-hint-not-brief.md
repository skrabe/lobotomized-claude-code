<!--
name: 'Slash Command: /design Sync Hint Is Not a Brief'
description: >-
  /design getPromptForCommand early-return telling the model that `sync <hint>`
  is the Design sync command and to have the user run /design-sync instead.
ccVersion: 2.1.265
variables:
  - SLASH_COMMAND_DESIGN_SYNC_HINT_NOT_BRIEF_VAR_0
-->
"sync ${SLASH_COMMAND_DESIGN_SYNC_HINT_NOT_BRIEF_VAR_0}" is the Claude Design sync command with a design-system hint, not a brief. Tell the user to run \`/design-sync ${SLASH_COMMAND_DESIGN_SYNC_HINT_NOT_BRIEF_VAR_0}\` instead (the dedicated command takes the hint) and stop — do not make anything.
