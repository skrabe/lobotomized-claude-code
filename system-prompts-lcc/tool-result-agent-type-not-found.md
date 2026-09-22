<!--
name: 'Tool Result: Agent type not found'
description: >-
  Error returned when the requested subagent_type does not match any available
  agent, listing the agent types that are available
ccVersion: 2.1.235
variables:
  - TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_0
  - TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_1
  - TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_2
-->
Agent type '${TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_0}' not found. Available agents: ${TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_1(TOOL_RESULT_AGENT_TYPE_NOT_FOUND_VAR_2)}
