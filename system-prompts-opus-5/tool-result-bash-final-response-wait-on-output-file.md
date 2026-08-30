<!--
name: 'Tool Result: Bash final response wait on output file'
description: >-
  Bash tool result when a backgrounded command is still running at
  final-response time, telling the model to wait on the output file instead of
  polling.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_0
  - TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_1
  - TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_2
-->
If you still need its result and have other work, keep working — it reaches you between your tool calls if it exits in time; if waiting for it is all that is left, wait with one foreground shell command that blocks until the output file shows what you need, rather than repeated ${TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_0} calls. Next time, run a command you must wait on in the foreground (with a timeout of up to ${TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_1.floor(TOOL_RESULT_BASH_FINAL_RESPONSE_WAIT_ON_OUTPUT_FILE_VAR_2()/60000)} minutes) and keep the background for work you can start and forget.
