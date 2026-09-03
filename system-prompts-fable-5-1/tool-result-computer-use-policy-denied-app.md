<!--
name: Computer-use policy-denied app
description: >-
  Tool-result telling the model an ungranted app is blocked by policy and cannot
  be used with computer use.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_POLICY_DENIED_APP_VAR_0
  - TOOL_RESULT_COMPUTER_USE_POLICY_DENIED_APP_VAR_1
-->
App ${TOOL_RESULT_COMPUTER_USE_POLICY_DENIED_APP_VAR_0(TOOL_RESULT_COMPUTER_USE_POLICY_DENIED_APP_VAR_1)??"(name withheld)"} is blocked by policy and cannot be used with computer use.
