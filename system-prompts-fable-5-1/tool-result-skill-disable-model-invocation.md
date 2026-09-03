<!--
name: 'Tool Result: Skill blocked by disable-model-invocation'
description: >-
  Skill-tool validateInput rejection returned to the model when it tries to
  invoke a skill marked disable-model-invocation; surfaced as <tool_use_error>
  content.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_1
  - TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_2
-->
Skill ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0} cannot be used with ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_1} tool due to disable-model-invocation. ${TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_2(TOOL_RESULT_SKILL_DISABLE_MODEL_INVOCATION_VAR_0)} Do not replicate this skill's workflow by other means — it is reserved for explicit user invocation.
