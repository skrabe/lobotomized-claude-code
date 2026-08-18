<!--
name: Auto-replies not resumed — generic failure
description: >-
  Fallback resume_replies tool result reporting the raw outcome and reason when
  the live watch could not be re-armed.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_GENERIC_FAILURE_VAR_0
-->
Auto-replies were NOT resumed (${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_GENERIC_FAILURE_VAR_0.outcome}${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_GENERIC_FAILURE_VAR_0.reason!==void 0?`: ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_GENERIC_FAILURE_VAR_0.reason}`:""}). The live watch could not be re-armed.
