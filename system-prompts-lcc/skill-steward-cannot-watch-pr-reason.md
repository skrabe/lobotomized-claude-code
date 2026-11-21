<!--
name: 'Skill: Steward cannot watch pull request'
description: >-
  Says the pull request can't be watched here, with reason and
  bypass-permissions advice
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_0
  - SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_1
  - SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_2
  - SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_3
  - SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_4
-->
I can't watch pull request #${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_0.binding.pr} here: ${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_1}.${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_2.mode==="bypassPermissions"?` ${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_3?"To have it watched, switch":"Switch"} to another permission mode (Shift+Tab), then run /${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_4}${SKILL_STEWARD_CANNOT_WATCH_PR_REASON_VAR_3?"":" again"}.`:""}
