<!--
name: 'Skill: Code review findings target floor'
description: >-
  Model-facing /code-review skill output instruction setting the minimum
  findings target (at least floor(N/2)) while telling the model not to invent
  findings to hit it.
ccVersion: 2.1.206
variables:
  - SKILL_CODE_REVIEW_OUTPUT_FINDINGS_TARGET_VAR_0
  - SKILL_CODE_REVIEW_OUTPUT_FINDINGS_TARGET_VAR_1
-->
## Output

Target **at least ${SKILL_CODE_REVIEW_OUTPUT_FINDINGS_TARGET_VAR_0.floor(SKILL_CODE_REVIEW_OUTPUT_FINDINGS_TARGET_VAR_1/2)} findings**. If fewer genuine findings exist, emit what you have — do not invent to hit the floor.
