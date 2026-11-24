<!--
name: 'Skill: Steward commit removed on GitHub'
description: >-
  Explains that the branch on GitHub no longer holds commits this checkout saw,
  so a push would restore them; tells the user how to proceed.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_0
  - SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_1
  - SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_2
  - SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_3
  - SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_4
-->
${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_0?.SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_1} on GitHub no longer has ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_2} that this checkout saw there earlier. Somebody may have taken ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_3} off on purpose, and a push would put ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_3} back. If you do want ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_3} there, run ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_4}. If you don't, take ${SKILL_STEWARD_PUSHED_COMMIT_REMOVED_ON_GITHUB_VAR_3} out of your branch. Then run
