<!--
name: 'Slash command: PR Steward terms protected-file merge left to user'
description: >-
  Says a base merge that would change Claude Code or git settings or .mcp.json
  is left to the user
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROTECTED_SETTINGS_MERGE_LEFT_TO_USER_VAR_0
-->
- If a check before that merge sees that it would change Claude Code's settings, .mcp.json, or git's own settings here${SLASH_COMMAND_PR_STEWARD_TERMS_PROTECTED_SETTINGS_MERGE_LEFT_TO_USER_VAR_0()?", or write to a path that this session's sandbox protects, such as the project's skills":""}, I'll leave it to you.
