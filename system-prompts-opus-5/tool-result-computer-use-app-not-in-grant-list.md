<!--
name: Computer-use app not in grant list
description: >-
  Tool-result telling the model the app is not in the granted-applications list
  and to call request_access first.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_NOT_IN_GRANT_LIST_VAR_0
  - TOOL_RESULT_COMPUTER_USE_APP_NOT_IN_GRANT_LIST_VAR_1
-->
App ${TOOL_RESULT_COMPUTER_USE_APP_NOT_IN_GRANT_LIST_VAR_0(TOOL_RESULT_COMPUTER_USE_APP_NOT_IN_GRANT_LIST_VAR_1)??"(name withheld)"} is not in the granted-applications list. Call request_access to ask the user for permission first.
