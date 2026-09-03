<!--
name: 'Tool Result: Remote Host Approval Withdrawn Race'
description: >-
  approval_not_received tool_result when the request was withdrawn but a delayed
  approval might have arrived first, so the model must check before retrying.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_RACE_VAR_0
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_WITHDRAWN_RACE_VAR_0}; the request was then withdrawn, but whether a delayed copy of the approval reached it first is not known. Check whether the command ran before retrying it.
