<!--
name: Skill disabled for model invocation
description: >-
  Error returned to the model via the Skill tool when the requested skill is
  disabled for model invocation.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_0
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_1
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_2
-->
Skill ${TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_0} is disabled for model invocation ${TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_1?TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_VAR_2?"by the disableBundledSkills setting or CLAUDE_CODE_DISABLE_BUNDLED_SKILLS env var, and by an explicit skillOverrides entry":"by the disableBundledSkills setting or CLAUDE_CODE_DISABLE_BUNDLED_SKILLS env var":"in skillOverrides settings"}
