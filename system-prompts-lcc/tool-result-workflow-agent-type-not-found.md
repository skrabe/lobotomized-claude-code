<!--
name: 'Tool result: workflow agent() type not found'
description: >-
  Workflow agent() error listing available agents when the requested agentType
  does not exist.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_0
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_1
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_2
-->
agent({agentType}): agent type '${TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_0}' not found. Available agents: ${TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_1.map((TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_2)=>TOOL_RESULT_WORKFLOW_AGENT_TYPE_NOT_FOUND_VAR_2.agentType).join(", ")}
