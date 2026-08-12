<!--
name: 'Tool result: Bash command auto-backgrounded on timeout'
description: >-
  Bash tool-result text returned to the model when a command exceeded its
  timeout and was moved to the background, with the output file path and how to
  check interim output.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_0
  - TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_1
  - TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_2
  - TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_3
  - TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_4
-->
Command did not complete within its ${TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_0.max(1,TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_0.round(TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_1/1000))}s timeout and was moved to the background (ID: ${TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_2}). Output is being written to: ${TOOL_RESULT_BASH_TIMED_OUT_BACKGROUNDED_VAR_3}.
