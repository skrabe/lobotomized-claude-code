<!--
name: 'Tool Result: AskUserQuestion Follow Up Required'
description: >-
  AskUserQuestion tool result telling the model to call the tool again with
  follow-up questions and not start the task yet.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_0
  - TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_1
  - TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_2
  - TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_3
-->
${TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_0} before you proceed. So far they answered: ${TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_1}.${TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_2} Call ${TOOL_RESULT_ASKUSERQUESTION_FOLLOW_UP_REQUIRED_VAR_3} again with follow-up questions that build on these answers (do not repeat these); do not start the task yet.
