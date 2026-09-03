<!--
name: 'Tool Result: Send Message Agent Resume In-Flight Missing'
description: >-
  SendMessage tool result when another caller is resuming the agent and its task
  record is gone, so the message was not delivered.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_IN_FLIGHT_MISSING_VAR_0
-->
${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_IN_FLIGHT_MISSING_VAR_0.agentName} is being resumed by another caller and its task record is gone; the message was not delivered. Retry shortly.
