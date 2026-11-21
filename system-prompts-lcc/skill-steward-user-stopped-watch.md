<!--
name: 'Skill: Steward user stopped watch'
description: >-
  After the user stops the watch, tells Claude to change nothing and report
  where the pull request stands
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_USER_STOPPED_WATCH_VAR_0
-->
The user stopped the watch, and its wake-up is cancelled. Change nothing. Tell the user in a line or two where the pull request stands, and: "Run /${SKILL_STEWARD_USER_STOPPED_WATCH_VAR_0} again to keep watching."
