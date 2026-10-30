<!--
name: 'Tool result: Send to project consent reason (existing project)'
description: >-
  Permission decisionReason for sending the brief to an existing Claude
  Project's memory and setup card.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_1
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_2
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_3
-->
With your Claude account, this brief is saved to the memory of ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_0!==null?`the Claude Project “${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_0}”`:TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_1} as ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_2}. It is posted as that project’s setup card. The project is told which Remote Control session it came from. ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_EXISTING_PROJECT_VAR_3}
