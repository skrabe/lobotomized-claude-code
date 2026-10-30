<!--
name: 'Tool Result: Send-to-project setup card uncertain'
description: >-
  Reports the setup card may or may not have been posted and that the brief was
  not handed to the coordinator
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_1
  - TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_2
-->
The setup card may or may not have been posted (${TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_0?.TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_1??"no answer"}). The coordinator was not handed the brief, so that the setup card is not posted twice. ${TOOL_RESULT_SEND_TO_PROJECT_SETUP_CARD_UNCERTAIN_VAR_2}
