<!--
name: 'Skill: Steward call review skill'
description: Instructs calling the review skill with TARGET and no other flag
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_0
  - SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_1
  - SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_2
-->
Call the ${SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_0} tool with \`skill: "${SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_1}"\` and \`args: "${SKILL_STEWARD_CALL_REVIEW_SKILL_INSTRUCTION_VAR_2} TARGET"\`, and no other flag.
