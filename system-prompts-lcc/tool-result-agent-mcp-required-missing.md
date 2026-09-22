<!--
name: Agent required MCP servers missing
description: >-
  Agent-tool launch error returned to the model when a required MCP server for
  the agent type is missing.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_0
  - TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_1
  - TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_2
-->
Agent '${TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_0.agentType}' requires MCP servers matching: ${TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_1.join(", ")}. MCP servers with tools: ${TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_2.length>0?TOOL_RESULT_AGENT_MCP_REQUIRED_MISSING_VAR_2.join(", "):"none"}. Use /mcp to configure and authenticate the required MCP servers.
