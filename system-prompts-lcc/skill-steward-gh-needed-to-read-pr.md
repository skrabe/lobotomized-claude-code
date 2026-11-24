<!--
name: 'Skill: Steward gh needed to read pull request'
description: Says gh is unavailable and is needed to read the named pull request
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_0
  - SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_1
  - SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_2
  - SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_3
-->
${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_0}, and ${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_1} needs it to read pull request #${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_2[2]}. Once gh works, run ${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_1} again.${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_2[1]===void 0?` ${SKILL_STEWARD_GH_NEEDED_TO_READ_PR_VAR_3}`:""}
