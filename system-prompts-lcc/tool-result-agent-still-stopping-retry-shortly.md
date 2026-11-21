<!--
name: 'Tool result: agent still stopping'
description: >-
  Refusal when messaging an agent still finishing its stop: retry in a few
  seconds or it gets ended.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_STILL_STOPPING_RETRY_SHORTLY_VAR_0
  - TOOL_RESULT_AGENT_STILL_STOPPING_RETRY_SHORTLY_VAR_1
-->
Agent ${TOOL_RESULT_AGENT_STILL_STOPPING_RETRY_SHORTLY_VAR_0} is still stopping, and can take a message in a few seconds. If it is still stopping then, ${TOOL_RESULT_AGENT_STILL_STOPPING_RETRY_SHORTLY_VAR_1} ends what is left of its run.
