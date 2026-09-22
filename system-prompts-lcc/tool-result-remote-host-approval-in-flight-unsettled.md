<!--
name: 'Tool Result: Remote Host Approval In Flight Unsettled'
description: >-
  Remote-host tool_result when the host was waiting on a permission decision and
  an answer may still arrive after restart.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_0(TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_1.host)} — ${TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_1.host} reports it was waiting on a permission decision there and nothing had run when asked, but an answer may still reach it, so whether it runs is not settled. Check its effect on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_IN_FLIGHT_UNSETTLED_VAR_1.host} before issuing it again, or ask the user.
