<!--
name: 'Tool Result: Agent waiting at permission prompt'
description: >-
  Agent tool result when a backgrounded agent is waiting for the user to answer
  a permission request
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_AGENT_WAITING_AT_PERMISSION_PROMPT_VAR_0
-->
The agent has not finished. It is waiting for the user to answer a permission request that is shown in the chat. What needs the permission has not run. The agent no longer blocks this turn. If the user allows the request, the agent continues, and a notification with its report arrives in a later message.
agentId: ${TOOL_RESULT_AGENT_WAITING_AT_PERMISSION_PROMPT_VAR_0.agentId} (internal ID, not shown to the user)
