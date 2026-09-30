<!--
name: Skill disabled for model invocation with policy reason
description: >-
  Error returned to the model via the Skill tool when a bundled skill is
  disabled for model invocation by organization policy, giving the policy's
  reason.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_0
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_1
  - TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_2
-->
Skill ${TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_0} is disabled for model invocation: ${TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_1}${TOOL_RESULT_SKILL_DISABLED_FOR_MODEL_POLICY_REASON_VAR_2?" It is also turned off by an explicit skillOverrides entry.":""}
