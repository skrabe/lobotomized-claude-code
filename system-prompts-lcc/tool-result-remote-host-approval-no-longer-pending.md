<!--
name: 'Tool Result: Remote Host Approval No Longer Pending'
description: >-
  Rebound: 2.1.288 merged the no-longer-pending and answers-different-request
  results into one template; the 'gone' branch comes first, so it keeps this id.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_PENDING_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_PENDING_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_PENDING_VAR_0==="gone"?`That permission request is no longer pending on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_PENDING_VAR_1}`:`This approval answers a different request than the one pending on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_NO_LONGER_PENDING_VAR_1}`}, so nothing ran. Run the tool again if it is still needed.
