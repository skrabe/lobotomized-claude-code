<!--
name: Remote Host Call Send Backed Up
description: >-
  Tool result when a remote call was withdrawn from the send queue because this
  session's connection was backed up.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_0
  - TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_1
  - TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_2
-->
The call to ${TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_0} could not be sent within ${TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_1.round(TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_2/1000)}s — this session's connection to the service was backed up — so it was withdrawn while still queued here. Most likely nothing ran on ${TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_0}: if the call reaches it late, its withdrawal arrives with it (for a command with side effects, check before repeating it). This is not a problem with ${TOOL_RESULT_REMOTE_HOST_CALL_SEND_BACKED_UP_VAR_0}; try the call again.
