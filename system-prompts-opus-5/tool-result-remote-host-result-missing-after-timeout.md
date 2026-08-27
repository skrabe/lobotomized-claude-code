<!--
name: Remote Host Result Missing After Timeout
description: >-
  Tool result when a remote call was sent but no result arrived and the host
  could not be reached afterwards.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_0
  - TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_1
  - TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_2
-->
The call was sent to ${TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_0}, but its result did not arrive within ${TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_1.round(TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_2/1000)}s and ${TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_0} could not be reached afterwards to ask; whether it ran, finished or failed there is not known. Check its effect on ${TOOL_RESULT_REMOTE_HOST_RESULT_MISSING_AFTER_TIMEOUT_VAR_0} before repeating it.
