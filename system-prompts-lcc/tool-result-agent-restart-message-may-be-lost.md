<!--
name: 'Tool result: agent not running at container restart'
description: >-
  SendMessage result when the target agent was not running at a container
  restart, so the message or answer may be lost.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_RESTART_MESSAGE_MAY_BE_LOST_VAR_0
-->
Agent ${TOOL_RESULT_AGENT_RESTART_MESSAGE_MAY_BE_LOST_VAR_0} was not running when the container was restarted. It may not have received this message, or its answer was lost. Ask it what it has done about this message before you send the work again.
