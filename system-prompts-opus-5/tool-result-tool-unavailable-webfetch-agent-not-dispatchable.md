<!--
name: 'Tool Result: WebFetch unavailable, web-fetch agent not dispatchable'
description: >-
  Suffix on the no-such-tool result explaining that WebFetch is unavailable here
  and the web-fetch subagent cannot be dispatched from this nesting depth, so
  the model should report the gap to its caller.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_DISPATCHABLE_VAR_0
  - TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_DISPATCHABLE_VAR_1
-->
. ${TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_DISPATCHABLE_VAR_0} is not available in this context, and the ${TOOL_RESULT_TOOL_UNAVAILABLE_WEBFETCH_AGENT_NOT_DISPATCHABLE_VAR_1} agent that reads web pages for this session cannot be dispatched from here (this agent's nesting depth or allowed subagent types rule it out). If the page is required, say so in your report so the caller can fetch it.
