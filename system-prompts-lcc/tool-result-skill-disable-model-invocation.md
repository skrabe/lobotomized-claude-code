<!--
name: 'Tool Result: Skill disable-model-invocation'
description: >-
  Skill tool error that a skill is reserved for explicit user invocation and
  must not be replicated by other means
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_1
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_2
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_3
-->
Skill ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0} cannot be used with ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_1} tool due to disable-model-invocation. ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_2(TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0,!1,TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_3)} Do not replicate this skill's workflow by other means — it is reserved for explicit user invocation.
