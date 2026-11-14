<!--
name: 'Tool Result: SendMessage agent not resumed with saved transcript'
description: >-
  Inline handback text naming the agent that was not resumed and quoting its
  final report from the saved transcript.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_1
-->
Agent ${TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_0} was not resumed, and your message was not delivered. It can still be resumed. Its final report, read from its saved transcript:

${TOOL_RESULT_SEND_MESSAGE_AGENT_NOT_RESUMED_SAVED_TRANSCRIPT_VAR_1}
