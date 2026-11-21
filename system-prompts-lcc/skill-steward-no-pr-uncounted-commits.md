<!--
name: 'Skill: Steward no pull request unknown commits'
description: >-
  No pull request and nothing pushed because it can't tell whether the branch
  has commits GitHub lacks
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_NO_PR_UNCOUNTED_COMMITS_VAR_0
-->
There is no pull request to watch, and I didn't push anything: nothing here is uncommitted, and I can't tell whether this branch holds commits that GitHub lacks. Check out the branch that holds your work, then run ${SKILL_STEWARD_NO_PR_UNCOUNTED_COMMITS_VAR_0} again.
