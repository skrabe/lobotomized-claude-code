<!--
name: 'Poll status: call not started, maybe permission'
description: >-
  Fragment saying an eval's tool call hasn't started and may be waiting for a
  permission answer.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_0
  - TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_1
  - TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_2
-->
its ${TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_0[0].toolName} call hasn't started after ${TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_1(TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_0[0].waitingMs)} (${TOOL_RESULT_POLL_STATUS_CALL_NOT_STARTED_PERMISSION_VAR_2} may be waiting for the user to answer a permission prompt)
