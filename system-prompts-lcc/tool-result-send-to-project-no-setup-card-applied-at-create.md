<!--
name: 'Tool Result: Send-to-project no setup card, applied at create'
description: >-
  Reports no setup card was posted because the brief fields were set at project
  creation
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_1
-->
No setup card was posted. The brief’s icon, color and instructions were set on the project when it was created, and it has no summary, threads or routines.${(TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_0.proposal.name??"")!==""?` The name it proposed, “${TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_1(TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_0.proposal.name??"")}”, was not used. The project is named “${TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_1(TOOL_RESULT_SEND_TO_PROJECT_NO_SETUP_CARD_APPLIED_AT_CREATE_VAR_0.projectName)}”, as you approved.`:""}
