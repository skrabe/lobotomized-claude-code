<!--
name: 'Skill: Steward merged branch with extra commits'
description: >-
  Refuses when the branch's pull request is merged but the branch still holds
  unmerged commits
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_MERGED_BRANCH_EXTRA_COMMITS_VAR_0
  - SKILL_STEWARD_MERGED_BRANCH_EXTRA_COMMITS_VAR_1
-->
Pull request #${SKILL_STEWARD_MERGED_BRANCH_EXTRA_COMMITS_VAR_0.pr} for this branch is merged, and the branch still holds commits that the default branch lacks, so a new pull request could show that work again. I did nothing. Move your work to a new branch cut from the default branch, then run ${SKILL_STEWARD_MERGED_BRANCH_EXTRA_COMMITS_VAR_1} again.
