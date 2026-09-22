<!--
name: Agent stopped by user
description: SendMessage tool-error returned to the model that the agent was user-stopped.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_0
-->
Agent "${TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_0.agentName}" was stopped by the user and was not resumed. Treat its work as cancelled; only start a new agent for it if the user explicitly asks.
