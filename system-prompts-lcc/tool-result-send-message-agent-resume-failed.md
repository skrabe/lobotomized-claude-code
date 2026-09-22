<!--
name: Agent resume failed
description: >-
  SendMessage tool-error returned to the model that a stopped agent could not be
  resumed.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_2
-->
Agent "${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_0.agentName}" is stopped (${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_0.status}) and could not be resumed: ${TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_1(TOOL_RESULT_SEND_MESSAGE_AGENT_RESUME_FAILED_VAR_2)}
