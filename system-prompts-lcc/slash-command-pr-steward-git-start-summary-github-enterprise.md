<!--
name: 'PR steward git start summary: GitHub Enterprise hint'
description: >-
  Start-summary line telling a possible GitHub Enterprise user to run gh auth
  login for the host so Claude can see checks and comments.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_GIT_START_SUMMARY_GITHUB_ENTERPRISE_VAR_0
  - SLASH_COMMAND_PR_STEWARD_GIT_START_SUMMARY_GITHUB_ENTERPRISE_VAR_1
-->
GitHub Enterprise? Run gh auth login --hostname ${SLASH_COMMAND_PR_STEWARD_GIT_START_SUMMARY_GITHUB_ENTERPRISE_VAR_0.replace(/:\d+$/,"")}, then ${SLASH_COMMAND_PR_STEWARD_GIT_START_SUMMARY_GITHUB_ENTERPRISE_VAR_1} again, and Claude sees checks and comments too.
