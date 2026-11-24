<!--
name: 'Slash command: Steward gh unreadable and git watch unavailable'
description: >-
  Reports gh can't read a pull request and a git-only watch isn't possible
  either
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_GH_UNREADABLE_NO_GIT_WATCH_VAR_0
-->
gh can't read a pull request from this checkout, and I can't watch the branch with git alone: ${SLASH_COMMAND_STEWARD_GIT_GH_UNREADABLE_NO_GIT_WATCH_VAR_0.say}.
