<!--
name: 'Tool Result: Unknown Skill Did You Mean Suggestion'
description: >-
  Skill-invoke tool_result when kind is suggestion, offering C.suggestion.name
  as the full skill name to invoke.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_SUGGESTION_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_SUGGESTION_VAR_1
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_SUGGESTION_VAR_0}. Did you mean ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_SUGGESTION_VAR_1.suggestion.name}? Invoke it by that full name.
