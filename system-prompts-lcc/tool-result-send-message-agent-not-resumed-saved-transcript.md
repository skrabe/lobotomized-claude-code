<!--
name: 'Tool result: SendMessage agent not resumed, saved transcript'
description: >-
  Inline handback text when the agent was not resumed, carrying its final report
  read from the saved transcript.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_1
-->
Agent ${TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_0} was not resumed, and your message was not delivered. A further message to it will try to resume the agent. Its final report, read from its saved transcript:

${TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_1}
