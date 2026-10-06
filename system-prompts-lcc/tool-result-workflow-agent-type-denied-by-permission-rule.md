<!--
name: 'Tool Result: workflow agent type denied by permission rule'
description: >-
  Error thrown into a workflow script when agent({agentType}) names an agent
  type denied by a permission rule, naming the rule and its source.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_0
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_1
  - TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_2
-->
agent({agentType}): '${TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_0}' is denied by permission rule '${TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_1}(${TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_0})' from ${TOOL_RESULT_WORKFLOW_AGENT_TYPE_DENIED_BY_PERMISSION_RULE_VAR_2.source}.
