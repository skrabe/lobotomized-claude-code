<!--
name: 'Tool Result: AskUserQuestion still listed, nobody to answer'
description: >-
  Suffix on the missing-tool error when AskUserQuestion is still listed but no
  one in the session can answer it. It tells the model to continue without it
  and ask in its response text instead.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_TOOL_UNAVAILABLE_STILL_LISTED_NO_ONE_TO_ANSWER_VAR_0
  - TOOL_RESULT_TOOL_UNAVAILABLE_STILL_LISTED_NO_ONE_TO_ANSWER_VAR_1
-->
. ${TOOL_RESULT_TOOL_UNAVAILABLE_STILL_LISTED_NO_ONE_TO_ANSWER_VAR_0} ${TOOL_RESULT_TOOL_UNAVAILABLE_STILL_LISTED_NO_ONE_TO_ANSWER_VAR_1}, but nobody in this session can answer it, so it cannot run. Continue without it; if you need the user's decision, ask in your response text instead.
