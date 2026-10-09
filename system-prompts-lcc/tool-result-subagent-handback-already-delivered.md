<!--
name: 'Tool Result: Subagent Handback Already Delivered'
description: >-
  SubagentHandback call() failure when a report was already delivered, steering
  further traffic to SendMessage.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_0
  - TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_1
  - TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_2
-->
Nothing was sent: your report was already delivered (${TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_0} delivers one report). ${TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_1()?"Stop now.":`Use ${TOOL_RESULT_SUBAGENT_HANDBACK_ALREADY_DELIVERED_VAR_2} for anything further, then stop.`}
