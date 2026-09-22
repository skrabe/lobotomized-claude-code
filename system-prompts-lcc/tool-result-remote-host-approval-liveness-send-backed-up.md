<!--
name: Remote Host Approval Liveness Send Backed Up
description: >-
  Tool result when a post-ask liveness check could not be sent because this
  session's connection was backed up.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_1
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_2
-->
The call had reached ${TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_0} and asked for approval there, but the check that ${TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_0} is still connected could not be sent within ${TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_1.round(TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_2/1000)}s — this session's connection to the service was backed up — so the user's approval was never sent and the pending request on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_0} is withdrawn; nothing ran. This is not a problem with ${TOOL_RESULT_REMOTE_HOST_APPROVAL_LIVENESS_SEND_BACKED_UP_VAR_0}; send the call again and the user will be asked once more.
