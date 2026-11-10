<!--
name: 'Tool result: SendMessage agent not resumed'
description: >-
  SendMessage result when the target agent was stopped/evicted and not resumed;
  treat its work as cancelled.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_1
-->
Agent "${TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_0}" ${TOOL_RESULT_SEND_MESSAGE_AGENT_STOPPED_VAR_1} and was not resumed. Treat its work as cancelled; only start a new agent for it if the user explicitly asks.
