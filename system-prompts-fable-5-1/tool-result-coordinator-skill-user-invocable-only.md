<!--
name: Coordinator skill user-invocable-only block
description: >-
  Meta message returned when a coordinator tries to run a
  disable-model-invocation skill that only the user may invoke.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_0
  - TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1
-->
Skill "/${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_0(TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1.name)}" is user-invocable only (${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_1.disableModelInvocation?"disable-model-invocation":"disabled for model invocation in settings"}) and cannot run in coordinator mode: the coordinator does not load skill content, and workers cannot invoke it via the ${TOOL_RESULT_COORDINATOR_SKILL_USER_INVOCABLE_ONLY_VAR_2} tool.
