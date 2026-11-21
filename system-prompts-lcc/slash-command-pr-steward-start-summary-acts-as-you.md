<!--
name: 'Slash command: PR Steward start summary acts as you'
description: >-
  Summarizes that Claude may comment, push to the head branch and merge the base
  as the user
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_0
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_1
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_2
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_3
-->
As you, Claude may comment and the like, push to ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_0}, and merge ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_1} into it${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_2(SLASH_COMMAND_PR_STEWARD_START_SUMMARY_ACTS_AS_YOU_VAR_3)?", with nobody looking":""}.
