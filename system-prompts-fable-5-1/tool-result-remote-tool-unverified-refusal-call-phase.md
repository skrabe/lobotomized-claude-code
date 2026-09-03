<!--
name: 'Tool Result: Remote Tool Unverified Refusal Call Phase'
description: >-
  host_unresponsive tool_result when an unverifiable reply says the session is
  no longer paired with the host, including whether the command may still be
  running.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_1
-->
A reply that could not be verified says this session is no longer paired with ${TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_0}. ${TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_1?"It was running there; whether it finished is unknown.":"The state of this command there is unknown — it may or may not have run."} Do not retry it on ${TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_0} until ${TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_0} re-announces; continue with what you can do without it, and tell the user you could not confirm whether it ${TOOL_RESULT_REMOTE_TOOL_UNVERIFIED_REFUSAL_CALL_PHASE_VAR_1?"finished":"ran"}.
