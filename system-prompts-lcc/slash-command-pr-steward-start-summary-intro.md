<!--
name: 'Slash command: PR Steward start summary intro'
description: >-
  Announces that the watch started for a pull request, for how many days and on
  the user's usage
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_0
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_1
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_2
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_3
-->
${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_0} started for ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_1}. Claude ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_2?"reviews your change, then watches":"watches"} the pull request for up to ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_INTRO_VAR_3} days, in this session, on your usage.
