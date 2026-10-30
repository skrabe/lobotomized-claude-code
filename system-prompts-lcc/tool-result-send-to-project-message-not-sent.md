<!--
name: 'Tool Result: Send-to-project message not sent'
description: Reports the message may not have arrived or was not sent
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_1
  - TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_2
-->
The message ${TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_0.outcome==="uncertain"?"may not have arrived":"was not sent"}${TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_1.aborted?"":` (${TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_2(TOOL_RESULT_SEND_TO_PROJECT_MESSAGE_NOT_SENT_VAR_0.failure)})`}.
