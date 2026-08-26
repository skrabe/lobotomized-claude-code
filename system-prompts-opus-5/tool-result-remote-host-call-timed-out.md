<!--
name: 'Tool Result: Remote Host Call Timed Out'
description: >-
  timed_out tool_result when the remote call exceeded the per-call limit; warns
  the command may still be running there.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_0
  - TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_1
  - TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_2
  - TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_3
-->
${TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_0} did not finish within ${TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_1.round(TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_2/1000)}s (the per-call limit for remote calls); the command may still be running there. Long-running commands belong ${TOOL_RESULT_REMOTE_HOST_CALL_TIMED_OUT_VAR_3()}.
