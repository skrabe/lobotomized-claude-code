<!--
name: 'Slash command: PR Steward terms base merge risk'
description: >-
  Warns that merging the base branch unattended lets anyone who lands a change
  there run programs with the user's credentials
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_VAR_0
-->
- I'll merge whatever has landed on ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_VAR_0} into your branch when needed, unattended, scripts that run by themselves included. So anyone who can land a change on ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_VAR_0} can run programs on this computer with your credentials while I watch.
