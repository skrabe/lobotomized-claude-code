<!--
name: AskUserQuestion Timeout — No Response
description: >-
  tool_result text returned when the user does not answer an AskUserQuestion in
  time, telling the model to proceed on best judgment and optionally re-ask
  later.
ccVersion: 2.1.199
variables:
  - TOOL_RESULT_ASK_USER_QUESTION_TIMEOUT_NO_RESPONSE_VAR_0
  - TOOL_RESULT_ASK_USER_QUESTION_TIMEOUT_NO_RESPONSE_VAR_1
-->
No response after ${TOOL_RESULT_ASK_USER_QUESTION_TIMEOUT_NO_RESPONSE_VAR_0.round(TOOL_RESULT_ASK_USER_QUESTION_TIMEOUT_NO_RESPONSE_VAR_1/1000)}s — the user may be away from keyboard. Proceed using your best judgment based on the context so far; you can re-ask this question later if it's still relevant.
