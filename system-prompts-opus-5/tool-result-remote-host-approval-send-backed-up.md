<!--
name: Remote Host Approval Send Backed Up
description: >-
  Tool result when the user's approval could not be forwarded because this
  session's connection was backed up.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_1
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_2
-->
The user's approval could not be sent to ${TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_0} within ${TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_1.round(TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_2/1000)}s — this session's connection to the service was backed up — so it was withdrawn while still queued here, and the pending request on ${TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_0} with it. Most likely nothing ran: if the approval still reaches ${TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_0} late, its cancellation arrives with it (for a command with side effects, check before repeating it). This is not a problem with ${TOOL_RESULT_REMOTE_HOST_APPROVAL_SEND_BACKED_UP_VAR_0}; send the call again and the user will be asked once more.
