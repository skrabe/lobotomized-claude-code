<!--
name: 'Slash command: PR Steward terms watch duration'
description: >-
  States how many days the watch runs and that it stops when the pull request is
  merged or closed
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_1
  - SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_2
-->
- ${SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_0?"Then I'll":"I'll"} watch ${SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_1} on my own for up to ${SLASH_COMMAND_PR_STEWARD_TERMS_WATCH_DURATION_VAR_2} days. I stop if it's merged or closed.
