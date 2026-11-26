<!--
name: 'Tool result: computer use access request unanswered'
description: >-
  Result when an access request's approval card closed with no answer; tells
  Claude to inform the user and not retry until they reply.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_2
-->
No response to the ${TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_0} request within the time limit, and its approval card has closed. The user did not decline it, and may not be at the computer. Tell the user ${TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_1}, and that replying here brings up a new card. Do not call ${TOOL_RESULT_COMPUTER_USE_ACCESS_REQUEST_UNANSWERED_VAR_2} again until they reply.
