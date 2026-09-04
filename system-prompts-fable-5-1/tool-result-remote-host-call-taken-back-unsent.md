<!--
name: 'Tool Result: Remote Host Call Taken Back Unsent'
description: >-
  Remote-host tool error when a stalled call was taken back before it left this
  session so the host never received it.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_0
  - TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_1
  - TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_2
-->
Nothing ran on ${TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_0}: the call could not be sent within ${TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_1.round(TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_2/1000)}s — this session's connection to the service was backed up — and it was taken back before it left this session, so ${TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_0} never received it. This is not a problem with ${TOOL_RESULT_REMOTE_HOST_CALL_TAKEN_BACK_UNSENT_VAR_0}; try the call again.
