<!--
name: 'Tool Result: WebFetch unavailable, web-fetch agent not allowed'
description: >-
  Suffix on the no-such-tool result for depth-0 sessions: WebFetch is
  unavailable and the web-fetch agent is outside the session's allowed subagent
  types, so the model should tell the user.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_ALLOWED_VAR_1
-->
. ${TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_ALLOWED_VAR_0} is not available in this context, and the ${TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_ALLOWED_VAR_1} agent that reads web pages for this session is outside this session's allowed subagent types. If the page is required, tell the user.
