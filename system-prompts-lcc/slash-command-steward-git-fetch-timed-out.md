<!--
name: 'Slash command: Steward git fetch timed out'
description: Reports that git couldn't fetch the base in time and suggests a manual fetch
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_1
-->
git couldn't fetch ${SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_0} from ${SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_1} in time (running git fetch ${SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_1} ${SLASH_COMMAND_STEWARD_GIT_FETCH_TIMED_OUT_VAR_0} yourself may help)
