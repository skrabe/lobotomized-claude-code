<!--
name: 'Tool Result: Remote Host Session Unreachable'
description: >-
  Remote tool call error when the named machine could not be reached from this
  session.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_0} could not be reached from this session (${TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_1}); the call did not run. If Claude is not running on ${TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_0}, or is no longer connected to this session, ask the user to check it; a call that was too large to deliver will not succeed on a retry.
