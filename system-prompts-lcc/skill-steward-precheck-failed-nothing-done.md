<!--
name: 'Skill: Steward precheck failed'
description: >-
  Says nothing was looked up or pushed because of a named problem, and to rerun
  once fixed
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_PRECHECK_FAILED_NOTHING_DONE_VAR_0
  - SKILL_STEWARD_PRECHECK_FAILED_NOTHING_DONE_VAR_1
-->
I didn't look for a pull request or push anything: ${SKILL_STEWARD_PRECHECK_FAILED_NOTHING_DONE_VAR_0}. Once that's fixed, run ${SKILL_STEWARD_PRECHECK_FAILED_NOTHING_DONE_VAR_1} again.
