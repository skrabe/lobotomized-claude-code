<!--
name: 'Tool Result: Remote tool approval requests pending limit reached'
description: >-
  Tool result telling Claude a machine already holds the maximum number of
  pending approval requests from this session, so the call was not asked about
  or run and should be resent after some are answered
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_2
-->
${TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_0} already has ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_1} approval ${TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_2(TOOL_RESULT_REMOTE_TOOL_APPROVAL_REQUESTS_PENDING_LIMIT_REACHED_VAR_1,"request")} from this session waiting, the most it holds at once, so it did not ask about this call and this call was not run. Send it again once some of them have been answered.
