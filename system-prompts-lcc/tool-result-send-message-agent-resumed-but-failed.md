<!--
name: 'Tool Result: SendMessage agent resumed but interrupted or failed'
description: >-
  SendMessage result saying the resumed agent was interrupted or failed while
  running, with the error.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_3
-->
Agent "${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_0}" was resumed but ${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_1?"was interrupted":"failed while running"}: ${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_2(TOOL_RESULT_SEND_MESSAGE_AGENT_RESUMED_BUT_FAILED_VAR_3)}
