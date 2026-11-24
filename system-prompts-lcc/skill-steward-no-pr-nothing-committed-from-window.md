<!--
name: 'Skill: Steward no PR, nothing committed from window'
description: >-
  Says the branch has no open PR and nothing was committed or pushed from this
  window (with the reason); open a PR yourself then run again.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_NO_PR_NOTHING_COMMITTED_FROM_WINDOW_VAR_0
  - SKILL_STEWARD_NO_PR_NOTHING_COMMITTED_FROM_WINDOW_VAR_1
-->
This branch has no open pull request, and I didn't commit or push anything from this window: ${SKILL_STEWARD_NO_PR_NOTHING_COMMITTED_FROM_WINDOW_VAR_0.say}. Open a pull request yourself, then run ${SKILL_STEWARD_NO_PR_NOTHING_COMMITTED_FROM_WINDOW_VAR_1} again.
