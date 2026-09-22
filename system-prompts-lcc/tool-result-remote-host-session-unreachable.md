<!--
name: 'Tool Result: Remote Host Session Unreachable'
description: >-
  unreachable tool_result on the session channel: the named machine could not be
  reached (detail in parentheses), so the call did not run and an oversized
  payload will not succeed on retry.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_0} could not be reached from this session (${TOOL_RESULT_REMOTE_HOST_SESSION_UNREACHABLE_VAR_1}); the call did not run. If its Claude Code is not running or not attached to this session, ask the user to check it; a call that was too large to deliver will not succeed on a retry.
