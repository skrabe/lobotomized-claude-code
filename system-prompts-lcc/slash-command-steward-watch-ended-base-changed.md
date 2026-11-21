<!--
name: 'Slash Command: Steward watch ended because base changed'
description: >-
  Says the pull request's base changed since the watch started and tells the
  user to run /steward again
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_WATCH_ENDED_BASE_CHANGED_VAR_0
-->
the pull request's base is no longer ${SLASH_COMMAND_STEWARD_WATCH_ENDED_BASE_CHANGED_VAR_0.baseRemote}/${SLASH_COMMAND_STEWARD_WATCH_ENDED_BASE_CHANGED_VAR_0.baseBranch}, as it was when the watch started. Tell the user to type /steward again to have it watched as it stands now
