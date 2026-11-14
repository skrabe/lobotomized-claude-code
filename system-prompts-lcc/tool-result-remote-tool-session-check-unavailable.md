<!--
name: 'Tool Result: Remote tool session check unavailable'
description: >-
  Tells the model a linked-computer tool call was not done because the session
  could not be checked with Anthropic's service, with retry guidance
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_SESSION_CHECK_UNAVAILABLE_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_SESSION_CHECK_UNAVAILABLE_VAR_0} could not check this session with Anthropic's service just now, so nothing was done for this request. That can pass: do other work, or wait, for about 45 seconds, then send the call again. If you have reason to think that it already ran or is still running, check that first. If it is refused this way three times, tell the user and continue without ${TOOL_RESULT_REMOTE_TOOL_SESSION_CHECK_UNAVAILABLE_VAR_0}.
