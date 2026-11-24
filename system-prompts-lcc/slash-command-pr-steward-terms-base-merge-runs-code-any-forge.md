<!--
name: 'Slash command: Steward terms base merge runs code (any forge)'
description: >-
  Warns that merging the base unattended lets others run programs with the
  user's credentials
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_1
-->
- On a conflict I'll merge ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_0} in, run the project's quick checks, and push as you. What somebody else pushes to ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_1} I'll take in. I've been told never to merge, approve or close the request. The merge brings whatever has landed on ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_0}, unattended, scripts that run by themselves included. So anyone who can land a change on ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_0}, or push to ${SLASH_COMMAND_PR_STEWARD_TERMS_BASE_MERGE_RUNS_CODE_ANY_FORGE_VAR_1}, can run programs on this computer with your credentials while I watch.
