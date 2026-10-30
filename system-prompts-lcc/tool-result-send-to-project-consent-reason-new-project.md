<!--
name: 'Tool result: Send to project consent reason (new project)'
description: >-
  Permission decisionReason for creating a new Claude Project from the brief,
  listing what is created, saved to memory and posted as the setup card.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_1
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_2
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_3
-->
With your Claude account, a Claude Project is created${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_0.length>0?` with the ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_1(TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_0)} from this brief`:""}. This repository’s GitHub origin may be added to it. This brief is saved to project memory as ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_2} and posted as the project’s setup card. The project is told which Remote Control session it came from. ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_NEW_PROJECT_VAR_3}
