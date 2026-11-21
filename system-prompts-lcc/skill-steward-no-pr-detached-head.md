<!--
name: 'Skill: Steward no pull request detached head'
description: No pull request because the checkout is not on a branch
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_NO_PR_DETACHED_HEAD_VAR_0
-->
There is no pull request to watch, and I didn't commit or push anything: you're not on a branch, as at a checked-out commit or a stop in a rebase. Check out your branch or finish your rebase, then run ${SKILL_STEWARD_NO_PR_DETACHED_HEAD_VAR_0} again.
