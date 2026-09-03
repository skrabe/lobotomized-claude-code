<!--
name: 'Tool Result: Remote Tool Request Withdrawn'
description: >-
  withdrawn/unanswerable message telling the model nothing ran on the host and
  not to retry without asking the user.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_2
-->
The request to run this on ${TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_0} was withdrawn — ${TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_1(TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_0,TOOL_RESULT_REMOTE_TOOL_REQUEST_WITHDRAWN_VAR_2)}; nothing ran there. Ask the user how to proceed rather than retrying.
