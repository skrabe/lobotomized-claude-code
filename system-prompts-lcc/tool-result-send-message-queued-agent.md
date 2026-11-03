<!--
name: 'Tool Result: SendMessage queued for agent'
description: Says the message is queued for the agent's next tool round
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_2
-->
Message queued for delivery to ${TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_0.agentName} at its next tool round.${TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_1}${TOOL_RESULT_SEND_MESSAGE_QUEUED_AGENT_VAR_2()?"":" If it finishes first, it is resumed with the message and notifies again, so wait for that notification before resending."}
