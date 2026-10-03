<!--
name: 'Skill: Code review findings target floor'
description: >-
  Model-facing /code-review skill output instruction setting a minimum findings
  target while telling the model not to invent findings to hit it
ccVersion: 2.1.288
variables:
  - MIN_FINDINGS_TARGET
  - PLURALIZE_FN
-->
## Output

Target **at least ${MIN_FINDINGS_TARGET} ${PLURALIZE_FN(MIN_FINDINGS_TARGET,"finding")}**. If fewer genuine findings exist, emit what you have — do not invent to hit the floor.
