<!--
name: 'Skill: Steward user stopped watch'
description: >-
  After the user stops the watch, tells Claude to change nothing and report
  where the pull request stands
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_0
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_1
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_2
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_3
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_4
-->
The user stopped the watch, and its wake-up is cancelled. ${SKILL_STEWARD_USER_STOPPED_WATCH_VAR_0?SKILL_STEWARD_USER_STOPPED_WATCH_VAR_1:""}${SKILL_STEWARD_USER_STOPPED_WATCH_VAR_2?SKILL_STEWARD_USER_STOPPED_WATCH_VAR_3:"Change nothing. Tell"} the user ${SKILL_STEWARD_USER_STOPPED_WATCH_VAR_0?"in a line or two where the pull request stands.":`that the watch has ended, in a line or two where the pull request stands, and: "Run /${SKILL_STEWARD_USER_STOPPED_WATCH_VAR_4} again to keep watching."`}
