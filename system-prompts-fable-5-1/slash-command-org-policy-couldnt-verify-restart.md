<!--
name: 'Slash Command: Org policy couldn''t verify restart'
description: >-
  Slash-command policy-gate reason when the org-policy cache missed, telling the
  model to restart Claude Code after checking the network.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_ORG_POLICY_COULDNT_VERIFY_RESTART_VAR_0
-->
Couldn't verify your organization's policy for ${SLASH_COMMAND_ORG_POLICY_COULDNT_VERIFY_RESTART_VAR_0.toLowerCase()}. Check your network connection, then restart Claude Code and try again.
