<!--
name: 'Steward: git watch stopped by user'
description: >-
  Prompt after the user stops a git-only watch: the wake-up is cancelled; tell
  the user where the branch stands.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_0
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_1
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_2
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_3
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_4
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_5
  - SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_6
-->
The user stopped the watch, and its wake-up is cancelled. ${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_0?SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_1:""}${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_2?SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_3:"Change nothing. Tell"} the user ${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_0?`in a line or two where ${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_4.headBranch} stands.`:`that the watch has ended, in a line or two where ${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_4.headBranch} stands, and: "Run /${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_5} ${SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_6(SKILL_STEWARD_GIT_USER_STOPPED_WATCH_VAR_4)} to keep watching."`}
