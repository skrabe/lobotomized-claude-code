<!--
name: 'Tool Result: Unknown Skill Did You Mean'
description: >-
  Skill-invoke tool_result when an ambiguous lookup has a single remaining
  candidate, suggesting that candidate's .name.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_VAR_1
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_VAR_0}. Did you mean ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_VAR_1.name}? Invoke it by that full name.
