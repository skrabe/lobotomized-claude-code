<!--
name: 'Slash command: Steward can''t watch branch here'
description: 'Says the branch can''t be watched here, with a permission-mode hint'
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_1
  - SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_2
-->
I can't watch this branch here: ${SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_0}.${SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_1?` Switch to another permission mode (Shift+Tab), then run /${SLASH_COMMAND_STEWARD_GIT_CANNOT_WATCH_BRANCH_HERE_VAR_2}.`:""}
