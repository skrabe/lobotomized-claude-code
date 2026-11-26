<!--
name: 'Skill: steward not put up review meanwhile'
description: >-
  Wrapper adding a pointer to run the review skill meanwhile after the
  nothing-pushed message
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_0
  - SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_1
  - SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_2
-->
${SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_0}${SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_1===0?` For a review meanwhile, run /${SKILL_STEWARD_NOT_PUT_UP_REVIEW_MEANWHILE_VAR_2}.`:""}
