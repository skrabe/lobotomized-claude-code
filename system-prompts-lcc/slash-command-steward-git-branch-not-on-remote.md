<!--
name: 'Slash command: Steward git branch not on remote'
description: Tells the user to push the branch to a remote under its own name first
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_BRANCH_NOT_ON_REMOTE_VAR_0
-->
${SLASH_COMMAND_STEWARD_GIT_BRANCH_NOT_ON_REMOTE_VAR_0} isn't on a remote yet under its own name: run git push -u REMOTE HEAD:refs/heads/${SLASH_COMMAND_STEWARD_GIT_BRANCH_NOT_ON_REMOTE_VAR_0} first
