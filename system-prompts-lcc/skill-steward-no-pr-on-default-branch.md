<!--
name: 'Skill: Steward no pull request on default branch'
description: No pull request and nothing pushed because the user is on the default branch
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_NO_PR_ON_DEFAULT_BRANCH_VAR_0
-->
There is no pull request to watch, and I didn't push anything: you're on the default branch, which ${SKILL_STEWARD_NO_PR_ON_DEFAULT_BRANCH_VAR_0} never pushes. Put your commits on a branch of their own (git switch -c my-change), then run ${SKILL_STEWARD_NO_PR_ON_DEFAULT_BRANCH_VAR_0} again.
