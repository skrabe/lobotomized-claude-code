<!--
name: Completed By Fallback Model
description: >-
  Local refusal-fallback note prepended to a subagent tool result, telling the
  parent model the response was completed by another model and the session model
  is unchanged.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_0
  - TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_1
  - TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_2
-->
${TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_0} This response was completed by ${TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_1}. Your session model is unchanged. ${TOOL_RESULT_SUBAGENT_REFUSAL_FALLBACK_COMPLETED_BY_VAR_2}
