<!--
name: 'Skill: Steward pull request already closed'
description: Says the pull request is already merged or closed
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_PR_ALREADY_CLOSED_VAR_0
  - SKILL_STEWARD_PR_ALREADY_CLOSED_VAR_1
-->
Pull request #${SKILL_STEWARD_PR_ALREADY_CLOSED_VAR_0.pr} is already ${SKILL_STEWARD_PR_ALREADY_CLOSED_VAR_0.state}, so ${SKILL_STEWARD_PR_ALREADY_CLOSED_VAR_1?"I didn't review or watch it":"there's nothing to watch"}.
