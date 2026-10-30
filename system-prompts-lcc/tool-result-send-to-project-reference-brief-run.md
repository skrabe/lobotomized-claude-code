<!--
name: 'Tool result: Send to project reference note (brief run)'
description: >-
  For-reference note on a brief run stating memory save, setup card status and
  that no thread was started.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_1
-->
For your reference only: ${TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_0.savedToMemory?`the brief is saved in project memory as ${TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_1}`:"nothing was saved to project memory"}; ${TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_0.setupSubmitted?"the setup card is posted":TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_0.handedOff?"the project’s coordinator was handed the brief and posts the setup card shortly":TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_BRIEF_RUN_VAR_0.setupUncertain===!0?"the setup card may or may not have been posted":"no setup card was posted"}; no thread was started.
