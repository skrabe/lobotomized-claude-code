<!--
name: Coordinator Skill User-Invocable-Only
description: >-
  Meta message injected when a coordinator tries to run a user-invocable-only
  skill that workers cannot invoke via the Skill tool.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_0
  - TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1
  - TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_2
-->
Skill "/${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_0(TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1.name)}" is user-invocable only (${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1.disableModelInvocation?"disable-model-invocation":"disabled for model invocation in settings"}) and cannot run in coordinator mode: the coordinator does not load skill content, and workers cannot invoke it via the ${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_2} tool.
